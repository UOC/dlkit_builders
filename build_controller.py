""" general controller for building things. Makes the builders configurable and
executable from the command line, not necessarily a Python shell.

Packages to build is read-in from config.py
"""
import os
import sys
import json
import glob
import textwrap

from collections import OrderedDict


from pattern_mapper import map_patterns
from xosid_mapper import XOsidMapper

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
ABS_PATH = os.path.abspath(os.path.join(PROJECT_PATH, os.pardir))


class Utilities(object):
    def _make_dir(self, target_dir):
        if ABS_PATH not in target_dir:
            target_dir = ABS_PATH + '/' + target_dir
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        return target_dir

    def _wrap(self, text):
        result = []
        wrapper = textwrap.TextWrapper(subsequent_indent=8*' ', width=80)
        for line in text.splitlines():
            result.append('\n'.join(wrapper.wrap(line)))
        return '\n'.join(result)

class BaseBuilder(Utilities):
    """base builder with some shared items, like package_maps dir, etc."""
    def __init__(self,
                 package_maps_dir='/builders/package_maps',
                 pattern_maps_dir='/builders/pattern_maps',
                 interface_maps_dir='/builders/interface_maps'):
        self._package_maps_dir = None
        self._pattern_maps_dir = None
        self._interface_maps_dir = None
        self._map_ext = '.json'
        self._abs_path = ABS_PATH

        self.package_maps = package_maps_dir
        self.pattern_maps = pattern_maps_dir
        self.interface_maps = interface_maps_dir
        super(BaseBuilder, self).__init__()

    def _package_file(self, package):
        if isinstance(package, dict) and 'name' in package:
            return self.package_maps + '/' + package['name'] + self._map_ext
        else:
            return self.package_maps + '/' + package + self._map_ext

    def _package_interface_file(self, package):
        if isinstance(package, dict) and 'name' in package:
            return self.interface_maps + '/' + package['name'] + self._map_ext
        else:
            # assume is package name string
            return self.interface_maps + '/' + package + self._map_ext

    def _package_pattern_file(self, package):
        return self.pattern_maps + '/' + package['name'] + self._map_ext

    def _pattern_map_exists(self, package):
        return self.first(package['name']) + self._map_ext in os.listdir(self.pattern_maps)

    @property
    def interface_maps(self):
        return self._interface_maps_dir

    @interface_maps.setter
    def interface_maps(self, interface_maps_dir):
        self._interface_maps_dir = self._make_dir(interface_maps_dir)

    @property
    def package_maps(self):
        return self._package_maps_dir

    @package_maps.setter
    def package_maps(self, package_maps_dir):
        self._package_maps_dir = self._make_dir(package_maps_dir)

    @property
    def pattern_maps(self):
        return self._pattern_maps_dir

    @pattern_maps.setter
    def pattern_maps(self, pattern_maps_dir):
        self._pattern_maps_dir = self._make_dir(pattern_maps_dir)

    def first(self, package_path):
        """a lot of builder patterns refer to the first item in a
        dot-separated path"""
        return package_path.split('.')[0]

    def grab_osid_name(self, xosid_filepath):
        return xosid_filepath.split('/')[-1].split('.')[-2]

    def last(self, package_path):
        """a lot of builder patterns refer to the last item in a
        dot-separated path"""
        return package_path.split('.')[-1]

    def get_interface_module(self, pkg_name, interface_shortname, report_error=False):
        """This function returns the category, or 'module' for the interface in question
        By default it does not raise an exception, but can be called with report-
        error equals True so that you can track un-categorized interfaces.
        """
        category = 'UNKNOWN_MODULE'
        try:
            with open(self._package_interface_file(pkg_name), 'r') as read_file:
                index = json.load(read_file)
        except IOError:
            if report_error:
                print ('INTERFACE LOOKUP ERROR - interface map for \'' + pkg_name +
                       '.' + interface_shortname + '\' not found.')
        else:
            try:
                category = index[pkg_name + '.' + interface_shortname]
            except KeyError:
                if report_error:
                    print ('INTERFACE LOOKUP ERROR - category for \'' + pkg_name + '.'
                           + interface_shortname + '\' not found.')
        return category


class PatternBuilder(XOsidMapper, BaseBuilder):
    def _make_impl_pattern_map(self, file_name=None, package=None, **kwargs):
        if package is None:
            package = self.map_xosid(file_name)
        self._make_dir(self.pattern_maps)
        pattern_index = OrderedDict()
        if package is not None:
            pattern_index = map_patterns(package, pattern_index, **kwargs)
            with open(self._package_pattern_file(package), 'w') as write_file:
                json.dump(pattern_index, write_file, indent=3)
        return True

    def make_patterns(self):
        sub_packages = []

        if self.package_maps[-1] != '/':
            json_pattern = self.package_maps + '/*.json'
        else:
            json_pattern = self.package_maps + '*.json'

        for json_file in glob.glob(json_pattern):
            with open(json_file, 'r') as read_file:
                package = json.load(read_file)

            if len(package['name'].split('.')) > 1:
                sub_packages.append(package)
            else:
                self._make_impl_pattern_map(package=package)

        for package in sub_packages:
            if self._pattern_map_exists(package):
                with open(self._package_pattern_file(package), 'r') as read_file:
                    base_package = json.load(read_file)

                self._make_impl_pattern_map(package=package,
                                            base_package=base_package)
            else:
                print 'Could not find pattern map' + \
                      self.first(package['name']) + \
                      'required for processing package' + \
                      package['name']


class Builder(Utilities):
    def __init__(self, build_dir='./dlkit/'):
        """configure the builder"""
        self._build_to_dir = None
        self.build_dir = build_dir
        self._xosid_dir = './xosid/'
        super(Builder, self).__init__()

    @property
    def build_dir(self):
        return self._build_to_dir

    @build_dir.setter
    def build_dir(self, value):
        self._build_to_dir = self._make_dir(value)

    def abc(self):
        from abcbinder import ABCBuilder
        ABCBuilder(build_dir=self.build_dir).make_abcosids()

    def map(self):
        """map all the xosid files"""
        from mappers import Mapper
        print "Mapping OSIDs"
        Mapper().map_all('all')

    def patterns(self):
        print "Creating pattern files"
        PatternBuilder().make_patterns()

if __name__ == '__main__':

    def usage():
        print "Usage: python build_controller.py [commands]"
        print "where:"
        print "  [commands] is any set of supported commands"
        print ""
        print "Supported commands:"
        print "  map: map the xosid files into pattern_maps/ and package_maps/"
        print "  abc: build the abstract_osids"
        print "  patterns: build the patterns"
        print "  mdata: build the metadata files"
        print "  authz: build the authz_adapter impl"
        print "  mongo: build the mongo OSID impl"
        print "  dlkit: build the dlkit convenience service impls"
        print "  tests: build the tests"
        print "  --all: build all of the above"
        print "  --buildto <directory>: the target build-to directory"
        print ""
        print "This searches the ./xosid/ directory for *.xosid files, which are parsed into code."
        print ""
        print "This will build the files to the directory specified, default of ./dlkit/."
        print ''
        print "examples:"
        print "  python build_controller.py map patterns abc mdata mongo"
        print "  python build_controller.py --all"

    if len(sys.argv) == 1:
        usage()
    else:
        builder = Builder()
        commands = ['--all',
                    '--buildto',
                    'map',
                    'patterns',
                    'abc',
                    'mdata',
                    'mongo',
                    'authz',
                    'dlkit',
                    'tests']
        if not any(c in sys.argv for c in commands):
            usage()
            sys.exit(1)

        # check that a follow-on directory to --buildto exists
        target_dir = None
        if '--buildto' in sys.argv:
            try:
                target_dir = sys.argv[sys.argv.index('--buildto') + 1]
            except IndexError:
                # no follow-on directory
                usage()
                sys.exit(1)
            else:
                if target_dir in commands:
                    usage()
                    sys.exit(1)
                builder.build_dir = target_dir

        if '--all' in sys.argv:
            # ignore the other commands
            builder.map()
            builder.patterns()
            builder.abc()
            pass
        else:
            # need to do these in a specific order, regardless of how
            # they are passed in.
            if 'map' in sys.argv:
                builder.map()
            if 'patterns' in sys.argv:
                builder.patterns()
            if 'abc' in sys.argv:
                builder.abc()
    sys.exit(0)
