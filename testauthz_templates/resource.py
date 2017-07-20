"""TestAuthZ templates for ${object_name_under} interfaces"""

class ResourceLookupSession:

    import_statements_pattern = [
        'import datetime',
        'import pytest',
        'import unittest  # Do we need this?',
        'from ....utilities.general import is_never_authz, is_no_authz, uses_cataloging',
        'from dlkit.abstract_osid.authorization import objects as ABCObjects',
        'from dlkit.abstract_osid.authorization import queries as ABCQueries',
        'from dlkit.abstract_osid.authorization.objects import Authorization',
        'from dlkit.abstract_osid.authorization.objects import AuthorizationList',
        'from dlkit.abstract_osid.authorization.objects import Vault as ABCVault',
        'from dlkit.abstract_osid.osid import errors',
        'from dlkit.abstract_osid.osid.objects import OsidCatalogForm, OsidCatalog',
        'from dlkit.abstract_osid.osid.objects import OsidForm',
        'from dlkit.primordium.calendaring.primitives import DateTime',
        'from dlkit.primordium.id.primitives import Id',
        'from dlkit.primordium.type.primitives import Type',
        'from dlkit.runtime import PROXY_SESSION, proxy_example',
        'from dlkit.runtime.managers import Runtime',
    ]

    init_template = """

REQUEST = proxy_example.SimpleRequest()
CONDITION = PROXY_SESSION.get_proxy_condition()
CONDITION.set_http_request(REQUEST)
PROXY = PROXY_SESSION.get_proxy(CONDITION)

LOOKUP_${object_name_upper}_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': '${pkg_name}.${object_name}', 'authority': 'ODL.MIT.EDU'})
SEARCH_${object_name_upper}_FUNCTION_ID = Id(**{'identifier': 'search', 'namespace': '${pkg_name}.${object_name}', 'authority': 'ODL.MIT.EDU'})
CREATE_${object_name_upper}_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': '${pkg_name}.${object_name}', 'authority': 'ODL.MIT.EDU'})
DELETE_${object_name_upper}_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': '${pkg_name}.${object_name}', 'authority': 'ODL.MIT.EDU'})
ASSIGN_${object_name_upper}_FUNCTION_ID = Id(**{'identifier': 'assign', 'namespace': '${pkg_name}.${object_name}${cat_name}', 'authority': 'ODL.MIT.EDU'})
CREATE_${cat_name_upper}_FUNCTION_ID = Id(**{'identifier': 'create', 'namespace': '${pkg_name}.${cat_name}', 'authority': 'ODL.MIT.EDU'})
DELETE_${cat_name_upper}_FUNCTION_ID = Id(**{'identifier': 'delete', 'namespace': '${pkg_name}.${cat_name}', 'authority': 'ODL.MIT.EDU'})
LOOKUP_${cat_name_upper}_FUNCTION_ID = Id(**{'identifier': 'lookup', 'namespace': '${pkg_name}.${cat_name}', 'authority': 'ODL.MIT.EDU'})
ACCESS_${cat_name_upper}_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'access', 'namespace': '${pkg_name}.${cat_name}', 'authority': 'ODL.MIT.EDU'})
MODIFY_${cat_name_upper}_HIERARCHY_FUNCTION_ID = Id(**{'identifier': 'modify', 'namespace': '${pkg_name}.${cat_name}', 'authority': 'ODL.MIT.EDU'})
ROOT_QUALIFIER_ID = Id('${pkg_name}.${cat_name}%3AROOT%40ODL.MIT.EDU')
BOOTSTRAP_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='bootstrap_vault')
OVERRIDE_VAULT_TYPE = Type(authority='ODL.MIT.EDU', namespace='authorization.Vault', identifier='override_vault')
DEFAULT_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'DEFAULT', 'authority': 'DEFAULT'})
DEFAULT_GENUS_TYPE = Type(**{'identifier': 'DEFAULT', 'namespace': 'GenusType', 'authority': 'DLKIT.MIT.EDU'})
ALIAS_ID = Id(**{'identifier': 'ALIAS', 'namespace': 'ALIAS', 'authority': 'ALIAS'})
AGENT_ID = Id(**{'identifier': 'jane_doe', 'namespace': 'osid.agent.Agent', 'authority': 'MIT-ODL'})
NEW_TYPE = Type(**{'identifier': 'NEW', 'namespace': 'MINE', 'authority': 'YOURS'})
NEW_TYPE_2 = Type(**{'identifier': 'NEW 2', 'namespace': 'MINE', 'authority': 'YOURS'})


@pytest.fixture(scope="class",
                params=['TEST_SERVICE'])
def authorization_session_class_fixture(request):
    request.cls.service_config = request.param
    request.cls.authz_mgr = Runtime().get_manager(
        'AUTHORIZATION',
        implementation='JSON_1')
    if not is_never_authz(request.cls.service_config):
        request.cls.vault_admin_session = request.cls.authz_mgr.get_vault_admin_session()
        request.cls.vault_lookup_session = request.cls.authz_mgr.get_vault_lookup_session()

        create_form = request.cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Vault'
        create_form.description = 'Test Vault for AuthorizationSession tests'
        create_form.genus_type = BOOTSTRAP_VAULT_TYPE
        request.cls.vault = request.cls.vault_admin_session.create_vault(create_form)

        create_form = request.cls.vault_admin_session.get_vault_form_for_create([])
        create_form.display_name = 'Test Override Vault'
        create_form.description = 'Test Override Vault for AuthorizationSession tests'
        create_form.genus_type = OVERRIDE_VAULT_TYPE
        request.cls.override_vault = request.cls.vault_admin_session.create_vault(create_form)

        request.cls.authz_admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(request.cls.vault.ident)
        request.cls.override_authz_admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(request.cls.override_vault.ident)
        request.cls.authz_lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(request.cls.vault.ident)

        # Set up ${cat_name} create authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_${cat_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${cat_name} Create for ${cat_name} AuthZ'
        create_form.description = '${cat_name} Create Authorization for ${cat_name} AuthZ tests'
        ${cat_name_under}_create_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${cat_name} delete authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_${cat_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${cat_name} Delete for ${cat_name} AuthZ'
        create_form.description = '${cat_name} Delete Authorization for ${cat_name} AuthZ tests'
        ${cat_name_under}_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${cat_name} lookup authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_${cat_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${cat_name} Lookup for ${cat_name} AuthZ'
        create_form.description = '${cat_name} Lookup Authorization for AuthorizationSession tests'
        ${cat_name_under}_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${cat_name} hierarchy access authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ACCESS_${cat_name_upper}_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${cat_name} Hierarchy Access for ${cat_name} AuthZ'
        create_form.description = '${cat_name} Hierarchy Access Authorization for AuthorizationSession tests'
        ${cat_name_under}_hierarchy_modify_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${cat_name} hierarchy modify authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            MODIFY_${cat_name_upper}_HIERARCHY_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${cat_name} Hierarchy Modify for ${cat_name} AuthZ'
        create_form.description = '${cat_name} Hierarchy Modify Authorization for AuthorizationSession tests'
        ${cat_name_under}_hierarchy_modify_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${object_name} create authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            CREATE_${object_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${object_name} create for ${cat_name} AuthZ'
        create_form.description = '${object_name} create Authorization for AuthorizationSession tests'
        ${object_name}_create_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${object_name} delete authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            DELETE_${object_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${object_name} Delete for ${cat_name} AuthZ'
        create_form.description = '${object_name} Delete Authorization for AuthorizationSession tests'
        ${object_name_under}_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${object_name} - ${cat_name} assignment authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            ASSIGN_${object_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${object_name} Delete for ${cat_name} AuthZ'
        create_form.description = '${object_name} Delete Authorization for AuthorizationSession tests'
        ${object_name_under}_delete_authz = request.cls.authz_admin_session.create_authorization(create_form)

        # Set up ${object_name} lookup authorization for current user
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            PROXY.get_authentication().get_agent_id(),
            LOOKUP_${object_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = '${object_name} Lookup for ${cat_name} AuthZ'
        create_form.description = '${object_name} Lookup Authorization for AuthorizationSession tests'
        ${object_name_under}_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)

        request.cls.${cat_name_under}_list = list()
        request.cls.${cat_name_under}_id_list = list()
        request.cls.authz_list = list()
        request.cls.authz_id_list = list()
        request.cls.${pkg_name}_mgr = Runtime().get_service_manager(
            '${pkg_name_replaced_upper}',
            proxy=PROXY,
            implementation='TEST_SERVICE')
        for num in [0, 1, 2, 3, 4, 5, 6, 7]:
            create_form = request.cls.${pkg_name}_mgr.get_${cat_name_under}_form_for_create([])
            create_form.display_name = 'Test ${cat_name} ' + str(num)
            create_form.description = 'Test ${cat_name} for Testing Authorization Number: ' + str(num)
            ${cat_name_under} = request.cls.${pkg_name}_mgr.create_${cat_name_under}(create_form)
            request.cls.${cat_name_under}_list.append(${cat_name_under})
            request.cls.${cat_name_under}_id_list.append(${cat_name_under}.ident)

        request.cls.${pkg_name}_mgr.add_root_${cat_name_under}(request.cls.${cat_name_under}_id_list[0])
        request.cls.${pkg_name}_mgr.add_child_${cat_name_under}(request.cls.${cat_name_under}_id_list[0], request.cls.${cat_name_under}_id_list[1])
        request.cls.${pkg_name}_mgr.add_child_${cat_name_under}(request.cls.${cat_name_under}_id_list[0], request.cls.${cat_name_under}_id_list[2])
        request.cls.${pkg_name}_mgr.add_child_${cat_name_under}(request.cls.${cat_name_under}_id_list[1], request.cls.${cat_name_under}_id_list[3])
        request.cls.${pkg_name}_mgr.add_child_${cat_name_under}(request.cls.${cat_name_under}_id_list[1], request.cls.${cat_name_under}_id_list[4])
        request.cls.${pkg_name}_mgr.add_child_${cat_name_under}(request.cls.${cat_name_under}_id_list[2], request.cls.${cat_name_under}_id_list[5])

        request.cls.svc_mgr = Runtime().get_service_manager(
            'AUTHORIZATION',
            proxy=PROXY,
            implementation=request.cls.service_config)
        request.cls.catalog = request.cls.svc_mgr.get_vault(request.cls.vault.ident)

        # Set up ${cat_name} lookup authorization for Jane
        create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
            AGENT_ID,
            LOOKUP_${cat_name_upper}_FUNCTION_ID,
            ROOT_QUALIFIER_ID,
            [])
        create_form.display_name = 'Jane Lookup Authorization'
        create_form.description = 'Test Authorization for AuthorizationSession tests'
        jane_lookup_authz = request.cls.authz_admin_session.create_authorization(create_form)
        request.cls.authz_list.append(jane_lookup_authz)
        request.cls.authz_id_list.append(jane_lookup_authz.ident)

        # Set up ${object_name} lookup authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_${object_name_upper}_FUNCTION_ID,
                request.cls.${cat_name_under}_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up ${object_name} lookup override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                LOOKUP_${object_name_upper}_FUNCTION_ID,
                request.cls.${cat_name_under}_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up ${object_name} search override authorizations for Jane
        for num in [7]:
            create_form = request.cls.override_authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_${object_name_upper}_FUNCTION_ID,
                request.cls.${cat_name_under}_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num) + ' (override)'
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.override_authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

        # Set up ${object_name} search authorizations for Jane
        for num in [1, 5]:
            create_form = request.cls.authz_admin_session.get_authorization_form_for_create_for_agent(
                AGENT_ID,
                SEARCH_${object_name_upper}_FUNCTION_ID,
                request.cls.${cat_name_under}_id_list[num],
                [])
            create_form.display_name = 'Test Authorization ' + str(num)
            create_form.description = 'Test Authorization for AuthorizationSession tests'
            authz = request.cls.authz_admin_session.create_authorization(create_form)
            request.cls.authz_list.append(authz)
            request.cls.authz_id_list.append(authz.ident)

    else:
        request.cls.catalog = request.cls.svc_mgr.get_authorization_session(proxy=PROXY)

    def class_tear_down():
        if not is_never_authz(request.cls.service_config):
            for catalog in request.cls.${pkg_name}_mgr.get_${cat_name_under}s():
                for obj in catalog.get_${object_name_under_plural}():
                    catalog.delete_${object_name_under}(obj.ident)
                request.cls.${pkg_name}_mgr.delete_${cat_name_under}(catalog.ident)
            for vault in request.cls.vault_lookup_session.get_vaults():
                lookup_session = request.cls.authz_mgr.get_authorization_lookup_session_for_vault(vault.ident)
                admin_session = request.cls.authz_mgr.get_authorization_admin_session_for_vault(vault.ident)
                for authz in lookup_session.get_authorizations():
                    admin_session.delete_authorization(authz.ident)
                request.cls.vault_admin_session.delete_vault(vault.ident)

        # The hierarchy should look like this. (t) indicates where lookup is
        # explicitely authorized:
        #
        #            _____ 0 _____
        #           |             |
        #        _ 1(t) _         2     not in hierarchy
        #       |        |        |
        #       3        4       5(t)      6     7(t)   (the 'blue' ${object_name_under} in ${cat_name_under} 2 is also assigned to ${cat_name_under} 7)

    request.addfinalizer(class_tear_down)


@pytest.fixture(scope="function")
def authorization_session_test_fixture(request):
    request.cls.session = request.cls.catalog


@pytest.mark.usefixtures("authorization_session_class_fixture", "authorization_session_test_fixture")
class TestAuthorizationSession(object):
    \"\"\"Tests for AuthorizationSession\"\"\"
    def test_get_vault_id(self):
        \"\"\"Tests get_vault_id\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.get_vault_id() == self.catalog.ident

    def test_get_vault(self):
        \"\"\"Tests get_vault\"\"\"
        # is this test really needed?
        if not is_never_authz(self.service_config):
            assert isinstance(self.catalog.get_vault(), ABCVault)

    def test_can_access_authorizations(self):
        \"\"\"Tests can_access_authorizations\"\"\"
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.can_access_authorizations()

    def test_is_authorized(self):
        \"\"\"Tests is_authorized\"\"\"
        if not is_never_authz(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[0])

    def test_is_authorized_1(self):
        \"\"\"Tests is_authorized 1\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[1])

    def test_is_authorized_3(self):
        \"\"\"Tests is_authorized 3\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[3])

    def test_is_authorized_4(self):
        \"\"\"Tests is_authorized 4\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[4])

    def test_is_authorized_2(self):
        \"\"\"Tests is_authorized 2\"\"\"
        if not is_never_authz(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[2])

    def test_is_authorized_5(self):
        \"\"\"Tests is_authorized 5\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[5])

    def test_is_authorized_6(self):
        \"\"\"Tests is_authorized 5\"\"\"
        if not is_never_authz(self.service_config):
            assert not self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[6])

    def test_is_authorized_7(self):
        \"\"\"Tests is_authorized 5\"\"\"
        if not is_never_authz(self.service_config):
            assert self.catalog.is_authorized(AGENT_ID, LOOKUP_${object_name_upper}_FUNCTION_ID, self.${cat_name_under}_id_list[7])

    def test_get_authorization_condition(self):
        \"\"\"Tests get_authorization_condition\"\"\"
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.get_authorization_condition(True)

    def test_is_authorized_on_condition(self):
        \"\"\"Tests is_authorized_on_condition\"\"\"
        if is_never_authz(self.service_config):
            pass  # no object to call the method on?
        elif uses_cataloging(self.service_config):
            pass  # cannot call the _get_record() methods on catalogs
        else:
            with pytest.raises(errors.Unimplemented):
                self.session.is_authorized_on_condition(True, True, True, True)

JANE_REQUEST = proxy_example.SimpleRequest(username='jane_doe')
JANE_CONDITION = PROXY_SESSION.get_proxy_condition()
JANE_CONDITION.set_http_request(JANE_REQUEST)
JANE_PROXY = PROXY_SESSION.get_proxy(JANE_CONDITION)

BLUE_TYPE = Type(authority='BLUE',
                 namespace='BLUE',
                 identifier='BLUE')


@pytest.fixture(scope="function")
def authz_adapter_class_fixture(request):
    request.cls.${object_name_under}_id_lists = []
    count = 0
    if not is_never_authz(request.cls.service_config):
        for ${cat_name_under}_ in request.cls.${cat_name_under}_list:
            request.cls.${object_name_under}_id_lists.append([])
            for color in ['Red', 'Blue', 'Red']:
                create_form = ${cat_name_under}_.get_${object_name_under}_form_for_create([])
                create_form.display_name = color + ' ' + str(count) + ' ${object_name}'
                create_form.description = color + ' ${object_name_under} for authz adapter tests from ${cat_name} number ' + str(count)
                if color == 'Blue':
                    create_form.genus_type = BLUE_TYPE
                ${object_name_under} = ${cat_name_under}_.create_${object_name_under}(create_form)
                if count == 2 and color == 'Blue':
                    request.cls.${pkg_name}_mgr.assign_${object_name_under}_to_${cat_name_under}(
                        ${object_name_under}.ident,
                        request.cls.${cat_name_under}_id_list[7])
                request.cls.${object_name_under}_id_lists[count].append(${object_name_under}.ident)
            count += 1

    def test_tear_down():
        if not is_never_authz(request.cls.service_config):
            for index, ${cat_name_under}_ in enumerate(request.cls.${cat_name_under}_list):
                for ${object_name_under}_id in request.cls.${object_name_under}_id_lists[index]:
                    ${cat_name_under}_.delete_${object_name_under}(${object_name_under}_id)

    request.addfinalizer(test_tear_down)


@pytest.mark.usefixtures("authz_adapter_class_fixture")
class Test${object_name}AuthzAdapter(TestAuthorizationSession):

    def test_lookup_${cat_name_under}_0_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            # with pytest.raises(errors.NotFound):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}()
            # with pytest.raises(errors.NotFound):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE)
            # for ${object_name_under}_id in self.${object_name_under}_id_lists[0]:
            #     with pytest.raises(errors.NotFound):
            #         ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)
            # with pytest.raises(errors.NotFound):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}_by_ids(self.${object_name_under}_id_lists[0])

    def test_lookup_${cat_name_under}_0_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.can_lookup_${object_name_under_plural}()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 1
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).next().ident == self.${object_name_under}_id_lists[2][1]
            ${cat_name_under}.get_${object_name_under}(self.${object_name_under}_id_lists[2][1])
            for ${object_name_under}_num in [0, 2]:
                with pytest.raises(errors.NotFound):  # Is this right?  Perhaps PermissionDenied
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(self.${object_name_under}_id_lists[2][${object_name_under}_num])

    def test_lookup_${cat_name_under}_0_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            # print "START"
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 13
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 5
            for ${object_name_under} in ${cat_name_under}.get_${object_name_under_plural}():
                ${cat_name_under}.get_${object_name_under}(${object_name_under}.ident)
            ${object_name_under}_ids = [${object_name_under}.ident for ${object_name_under} in ${cat_name_under}.get_${object_name_under_plural}()]
            ${cat_name_under}.get_${object_name_under_plural}_by_ids(${object_name_under}_ids)
            for ${object_name_under}_id in self.${object_name_under}_id_lists[0]:
                with pytest.raises(errors.NotFound):
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)
            ${object_name_under} = ${cat_name_under}.get_${object_name_under}(self.${object_name_under}_id_lists[2][1])
            for ${object_name_under}_num in [0, 2]:
                with pytest.raises(errors.NotFound):
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(self.${object_name_under}_id_lists[2][${object_name_under}_num])
            for ${object_name_under}_id in self.${object_name_under}_id_lists[1]:
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)
            for ${object_name_under}_id in self.${object_name_under}_id_lists[3]:
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)
            for ${object_name_under}_id in self.${object_name_under}_id_lists[4]:
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)
            for ${object_name_under}_id in self.${object_name_under}_id_lists[5]:
                    ${object_name_under} = ${cat_name_under}.get_${object_name_under}(${object_name_under}_id)

    def test_lookup_${cat_name_under}_0_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 0
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 0

    def test_lookup_${cat_name_under}_1_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_${cat_name_under}_1_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 9
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_${cat_name_under}_1_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 9
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 3

    def test_lookup_${cat_name_under}_1_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_${cat_name_under}_2_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[2])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 1
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}()
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE)

    def test_lookup_${cat_name_under}_2_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[2])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 1
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}()
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE)

    def test_lookup_${cat_name_under}_2_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[2])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 4
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 2
            # self.assertEqual(${cat_name_under}.get_${object_name_under_plural}().available(), 3)
            # self.assertEqual(${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available(), 1)

    def test_lookup_${cat_name_under}_2_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[2])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 1
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}()
            # with pytest.raises(errors.PermissionDenied):
            #     ${object_name_under_plural} = ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE)

    def test_lookup_${cat_name_under}_3_plenary_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[3])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_${cat_name_under}_3_plenary_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[3])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_plenary_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_${cat_name_under}_3_comparative_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[3])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_lookup_${cat_name_under}_3_comparative_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[3])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            ${cat_name_under}.use_comparative_${object_name_under}_view()
            assert ${cat_name_under}.get_${object_name_under_plural}().available() == 3
            assert ${cat_name_under}.get_${object_name_under_plural}_by_genus_type(BLUE_TYPE).available() == 1

    def test_query_${cat_name_under}_0_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            with pytest.raises(errors.PermissionDenied):
                query = ${cat_name_under}.get_${object_name_under}_query()

    def test_query_${cat_name_under}_0_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[0])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            query = ${cat_name_under}.get_${object_name_under}_query()
            query.match_display_name('red')
            assert ${cat_name_under}.get_${object_name_under_plural}_by_query(query).available() == 8
            query.clear_display_name_terms()
            query.match_display_name('blue')
            assert ${cat_name_under}.get_${object_name_under_plural}_by_query(query).available() == 5

    def test_query_${cat_name_under}_1_isolated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_isolated_${cat_name_under}_view()
            query = ${cat_name_under}.get_${object_name_under}_query()
            query.match_display_name('red')
            assert ${cat_name_under}.get_${object_name_under_plural}_by_query(query).available() == 2

    def test_query_${cat_name_under}_1_federated(self):
        if not is_never_authz(self.service_config):
            janes_${pkg_name}_mgr = Runtime().get_service_manager(
                '${pkg_name_upper}',
                proxy=JANE_PROXY,
                implementation='TEST_SERVICE_JSON_AUTHZ')
            ${cat_name_under} = janes_${pkg_name}_mgr.get_${cat_name_under}(self.${cat_name_under}_id_list[1])
            ${cat_name_under}.use_federated_${cat_name_under}_view()
            query = ${cat_name_under}.get_${object_name_under}_query()
            query.match_display_name('red')
            assert ${cat_name_under}.get_${object_name_under_plural}_by_query(query).available() == 6

"""