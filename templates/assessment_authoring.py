from .osid_managers import GenericAdapterProfileAndManager
from .osid_session import GenericAdapterSession


class AssessmentAuthoringProfile:
    init = {
        'python': {
            'authz': """
    def __init__(self):
        osid_managers.OsidProfile.__init__(self)

    def _get_hierarchy_session(self, proxy=None):
        base_package_mgr = self._get_base_package_provider_manager('assessment', proxy)
        if proxy is not None:
            try:
                return base_package_mgr.get_bank_hierarchy_session(proxy)
            except Unsupported:
                return None
        try:
            return base_package_mgr.get_bank_hierarchy_session()
        except Unsupported:
            return None

    def _get_base_package_provider_manager(self, base_package, proxy=None):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(base_package))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if proxy is not None:
            # need to add version argument
            return self._my_runtime.get_proxy_manager(base_package.upper(), provider_impl)
        else:
            # need to add version argument
            return self._my_runtime.get_manager(base_package.upper(), provider_impl)"""
        }
    }

    get_assessment_part_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    get_assessment_part_search_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    get_sequence_rule_enabler_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    get_sequence_rule_enabler_search_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    get_sequence_rule_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    get_sequence_rule_search_record_types = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_assessment_part_admin = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_assessment_part_lookup = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_assessment_part_item = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_assessment_part_item_design = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_sequence_rule_admin = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_sequence_rule_lookup = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }

    supports_assessment_part_query = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method_no_args['python']['services']
        }
    }


class AssessmentAuthoringManager:
    get_sequence_rule_lookup_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_sequence_rule_lookup_session_for_bank = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_lookup_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_lookup_session_for_bank = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_query_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_query_session_for_bank = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_admin_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_admin_session_for_bank = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_bank_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_assessment_part_bank_assignment_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_sequence_rule_admin_session = {
        'python': {
            'services': GenericAdapterProfileAndManager.sub_package_method['python']['services']
        }
    }

    get_sequence_rule_admin_session_for_bank = {
        'python': {
            'services': """
    def ${method_name}(self, *args, **kwargs):
        \"\"\"Pass through to provider method\"\"\"
        return self._get_sub_package_provider_manager('assessment_authoring').get_sequence_rule_admin_session_for_bank(*args, **kwargs)

    def get_assessment_part_item_session(self, *args, **kwargs):
        \"\"\"Pass through to provider method\"\"\"
        # Missing in the spec
        return self._get_sub_package_provider_manager('assessment_authoring').get_assessment_part_item_session(*args, **kwargs)

    def get_assessment_part_item_session_for_bank(self, *args, **kwargs):
        \"\"\"Pass through to provider method\"\"\"
        # Missing in the spec
        return self._get_sub_package_provider_manager('assessment_authoring').get_assessment_part_item_session_for_bank(*args, **kwargs)

    def get_assessment_part_item_design_session(self, *args, **kwargs):
        \"\"\"Pass through to provider method\"\"\"
        # Missing in the spec
        return self._get_sub_package_provider_manager('assessment_authoring').get_assessment_part_item_design_session(*args, **kwargs)

    def get_assessment_part_item_design_session_for_bank(self, *args, **kwargs):
        \"\"\"Pass through to provider method\"\"\"
        # Missing in the spec
        return self._get_sub_package_provider_manager('assessment_authoring').get_assessment_part_item_design_session_for_bank(*args, **kwargs)"""
        }
    }

    # The following is here only until Tom fixes spec and adds these methods
    additional_methods = {
        'python': {
            'json': """
    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_session(self, *args, **kwargs):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item service.

        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(runtime=self._runtime)

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_session_for_bank(self, bank_id, *args, **kwargs):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item()`` and
        ``supports_visible_federation()`` are ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(bank_id, runtime=self._runtime)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_design_session(self, *args, **kwargs):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item design service.

        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(runtime=self._runtime)

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    @utilities.remove_null_proxy_kwarg
    @utilities.arguments_not_none
    def get_assessment_part_item_design_session_for_bank(self, bank_id, *args, **kwargs):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item design service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        if self._proxy_in_args(*args, **kwargs):
            raise errors.InvalidArgument('A Proxy object was received but not expected.')

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(bank_id, runtime=self._runtime)""",
            'authz': """
    def get_assessment_part_item_session(self):
        return getattr(sessions, 'AssessmentPartItemSession')(
            provider_session=self._provider_manager.get_assessment_part_item_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    def get_assessment_part_item_session_for_bank(self, bank_id):
        return getattr(sessions, 'AssessmentPartItemSession')(
            provider_session=self._provider_manager.get_assessment_part_item_session_for_bank(bank_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    def get_assessment_part_item_design_session(self):
        return getattr(sessions, 'AssessmentPartItemDesignSession')(
            provider_session=self._provider_manager.get_assessment_part_item_design_session(),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    def get_assessment_part_item_design_session_for_bank(self, bank_id):
        return getattr(sessions, 'AssessmentPartItemDesignSession')(
            provider_session=self._provider_manager.get_assessment_part_item_design_session_for_bank(bank_id),
            authz_session=self._get_authz_session(),
            override_lookup_session=self._get_override_lookup_session(),
            provider_manager=self._provider_manager)"""
        }
    }


class AssessmentAuthoringProxyManager:

    # The following is here only until Tom fixes spec and adds these methods
    additional_methods = {
        'python': {
            'json': """
    @utilities.arguments_not_none
    def get_assessment_part_item_session(self, proxy):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item service.

        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(proxy=proxy, runtime=self._runtime)

    assessment_part_item_session = property(fget=get_assessment_part_item_session)

    @utilities.arguments_not_none
    def get_assessment_part_item_session_for_bank(self, bank_id, proxy):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemSession)
                - an ``AssessmentPartItemSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item()`` and
        ``supports_visible_federation()`` are ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemSession(bank_id, proxy=proxy, runtime=self._runtime)

    @utilities.arguments_not_none
    def get_assessment_part_item_design_session(self, proxy):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item design service.

        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_lookup()`` is ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(proxy=proxy, runtime=self._runtime)

    assessment_part_item_design_session = property(fget=get_assessment_part_item_design_session)

    @utilities.arguments_not_none
    def get_assessment_part_item_design_session_for_bank(self, bank_id, proxy):
        \"\"\"Gets the ``OsidSession`` associated with the assessment part item design service for the given bank.

        arg:    bank_id (osid.id.Id): the ``Id`` of the ``Bank``
        return: (osid.assessment.authoring.AssessmentPartItemDesignSession)
                - an ``AssessmentPartItemDesignSession``
        raise:  NotFound - no ``Bank`` found by the given ``Id``
        raise:  NullArgument - ``bank_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_assessment_part_item_design()`` or
                ``supports_visible_federation()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_assessment_part_item_design()`` and
        ``supports_visible_federation()`` are ``true``.*

        \"\"\"
        if not self.supports_assessment_part_lookup():  # This is kludgy, but only until Tom fixes spec
            raise errors.Unimplemented()

        # Also include check to see if the catalog Id is found otherwise raise errors.NotFound
        # pylint: disable=no-member
        return sessions.AssessmentPartItemDesignSession(bank_id, proxy=proxy, runtime=self._runtime)"""
        }
    }


class AssessmentPartLookupSession:
    get_assessment_part = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts_for_assessment = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts_by_genus_type = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts_by_parent_genus_type = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts_by_record_type = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_parts_by_ids = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    can_lookup_assessment_parts = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }

    use_sequestered_assessment_part_view = {
        'python': {
            'services': """
    def ${method_name}(self):
        \"\"\"Pass through to provider AssessmentPartLookupSession.use_sequestered_assessment_part_view\"\"\"
        # Does this need to be re-implemented to match the other non-sub-package view setters?
        self._containable_views['assessment_part'] = SEQUESTERED
        self._get_sub_package_provider_session('assessment_authoring',
                                               'assessment_part_lookup_session')
        for session in self._provider_sessions:
            for provider_session_name, provider_session in self._provider_sessions[session].items():
                try:
                    provider_session.use_sequestered_assessment_part_view()
                except AttributeError:
                    pass"""
        }
    }

    use_unsequestered_assessment_part_view = {
        'python': {
            'json': """
    def ${method_name}(self):
        \"\"\"Pass through to provider AssessmentPartLookupSession.use_unsequestered_assessment_part_view\"\"\"
        # Does this need to be re-implemented to match the other non-sub-package view setters?
        self._containable_views['assessment_part'] = UNSEQUESTERED
        self._get_sub_package_provider_session('assessment_authoring',
                                               'assessment_part_lookup_session')
        for session in self._provider_sessions:
            for provider_session_name, provider_session in self._provider_sessions[session].items():
                try:
                    provider_session.use_unsequestered_assessment_part_view()
                except AttributeError:
                    pass"""
        }
    }

    additional_methods = {
        'python': {
            'json': """
    @utilities.arguments_not_none
    def get_assessment_parts_for_assessment_part(self, assessment_part_id):
        \"\"\"Gets an ``AssessmentPart`` for the given assessment part.

        arg:    assessment_part_id (osid.id.Id): an assessment part ``Id``
        return: (osid.assessment.authoring.AssessmentPartList) - the
                returned ``AssessmentPart`` list
        raise:  NullArgument - ``assessment_part_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        \"\"\"
        # NOT IN SPEC - Implemented from
        # osid.assessment_authoring.AssessmentPartLookupSession.additional_methods
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentPartId': str(assessment_part_id)},
                 **self._view_filter()))
        return objects.AssessmentPartList(result, runtime=self._runtime)""",
            'authz': """

    def get_assessment_parts_for_assessment_part(self, assessment_part_id):
        # NOT CURRENTLY IN SPEC - Implemented from
        # osid.assessment_authoring.AssessmentPartLookupSession.additional_methods
        if self._can('lookup'):
            return self._provider_session.get_assessment_parts_for_assessment_part(assessment_part_id)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_assessment_part_query()
        query.match_assessment_part_id(assessment_part_id, match=True)
        return self._try_harder(query)"""
        }
    }


class AssessmentPartQuerySession:
    get_assessment_part_query = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }

    can_search_assessment_parts = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }


class AssessmentPartAdminSession:
    import_statements = {
        'python': {
            'json': [
                'from . import objects',
                'from dlkit.abstract_osid.osid import errors',
                'from dlkit.abstract_osid.assessment_authoring.objects import AssessmentPartForm as ABCAssessmentPartForm',
                'from dlkit.abstract_osid.id.primitives import Id as ABCId',
                'from dlkit.json_.assessment.assessment_utilities import get_assessment_part_lookup_session',
                'DESCENDING = -1',
                'ASCENDING = 1',
                'CREATED = True',
                'UPDATED = True',
                'ACTIVE = 0',
                'ANY_STATUS = 1',
                'SEQUESTERED = 0',
                'UNSEQUESTERED = 1',
            ]
        }
    }

    get_assessment_part_form_for_create_for_assessment = {
        'python': {
            'services': """
    def ${method_name}(self, *args, **kwargs):
        ${pattern_name}
        return self._get_sub_package_provider_session('assessment_authoring',
                                                      'assessment_part_admin_session').get_assessment_part_form_for_create_for_assessment(*args, **kwargs)"""
        }
    }

    can_create_assessment_parts = {
        'python': {
            'services': """
    def ${method_name}(self):
        \"\"\"Pass through to provider AssessmentPartAdminSession.can_create_assessment_parts\"\"\"
        ${pattern_name}
        return self._get_sub_package_provider_session('assessment_authoring',
                                                      'assessment_part_admin_session').can_create_assessment_parts()"""
        }
    }

    can_create_assessment_part_with_record_types = {
        'python': {
            'services': """
    def ${method_name}(self, *args, **kwargs):
        \"\"\"Pass through to provider AssessmentPartAdminSession.can_create_assessment_part_with_record_types\"\"\"
        ${pattern_name}
        return self._get_sub_package_provider_session('assessment_authoring',
                                                      'assessment_part_admin_session').can_create_assessment_part_with_record_types(*args, **kwargs)"""
        }
    }

    get_assessment_part_form_for_create_for_assessment_part = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id, assessment_part_record_types):
        ${doc_string}
        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('argument is not a valid OSID Id')
        for arg in assessment_part_record_types:
            if not isinstance(arg, ABCType):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID Type')
        if assessment_part_record_types == []:
            assessment_part_record_types = None
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session_for_bank(self._catalog_id, proxy=self._proxy)
        child_parts = lookup_session.get_assessment_parts_for_assessment_part(assessment_part_id)
        mdata = {}
        # Check for underlying Parts, whether Sections and set appropriate mdata overrides:
        if child_parts.available == 0:
            pass
        else:
            mdata['sequestered'] = {}
            mdata['sequestered']['is_read_only'] = True
            mdata['sequestered']['is_required'] = True
            if child_parts.available() > 0 and child_parts.next().is_section():
                mdata['sequestered']['default_boolean_values'] = [False]
            else:
                mdata['sequestered']['default_boolean_values'] = [True]
        # WHY are we passing bank_id = self._catalog_id below, seems redundant:
        obj_form = objects.AssessmentPartForm(
            bank_id=self._catalog_id,
            record_types=assessment_part_record_types,
            assessment_part_id=assessment_part_id,
            catalog_id=self._catalog_id,
            runtime=self._runtime,
            mdata=mdata)
        obj_form._for_update = False
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form""",
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_assessment_part_form_for_update = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id):
        ${doc_string}
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        if (assessment_part_id.get_identifier_namespace() != 'assessment_authoring.AssessmentPart' or
                assessment_part_id.get_authority() != self._authority):
            raise errors.InvalidArgument()
        result = collection.find_one({'_id': ObjectId(assessment_part_id.get_identifier())})

        mdata = {}
        if not result['assessmentPartId']:
            pass
        else:
            parent_part_id = Id(result['assessmentPartId'])
            mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
            lookup_session = mgr.get_assessment_part_lookup_session_for_bank(self._catalog_id, proxy=self._proxy)
            if lookup_session.get_assessment_parts_for_assessment_part(parent_part_id).available() > 1:
                mdata['sequestered']['is_read_only'] = True
                mdata['sequestered']['is_required'] = True
        obj_form = objects.AssessmentPartForm(osid_object_map=result,
                                              runtime=self._runtime,
                                              proxy=self._proxy,
                                              mdata=mdata)
        self._forms[obj_form.get_id().get_identifier()] = not UPDATED

        return obj_form""",
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    delete_assessment_part = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id):
        ${doc_string}
        # Should be implemented from template for
        # osid.learning.ObjectiveAdminSession.delete_objective_template
        # but need to handle magic part delete ...

        if not isinstance(assessment_part_id, ABCId):
            raise errors.InvalidArgument('the argument is not a valid OSID Id')
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if collection.find({'assessmentPartId': str(assessment_part_id)}).count() != 0:
            raise errors.IllegalState('there are still AssessmentParts associated with this AssessmentPart')

        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        try:
            apls = get_assessment_part_lookup_session(runtime=self._runtime,
                                                      proxy=self._proxy)
            apls.use_unsequestered_assessment_part_view()
            apls.use_federated_bank_view()
            part = apls.get_assessment_part(assessment_part_id)
            part.delete()
        except AttributeError:
            collection.delete_one({'_id': ObjectId(assessment_part_id.get_identifier())})""",
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    # Need to override the template because of the extra ``assessment_part_id`` argument
    update_assessment_part = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id, assessment_part_form):
        ${doc_string}
        collection = JSONClientValidated('assessment_authoring',
                                         collection='AssessmentPart',
                                         runtime=self._runtime)
        if not isinstance(assessment_part_form, ABCAssessmentPartForm):
            raise errors.InvalidArgument('argument type is not an AssessmentPartForm')
        if not assessment_part_form.is_for_update():
            raise errors.InvalidArgument('the AssessmentPartForm is for update only, not create')
        try:
            if self._forms[assessment_part_form.get_id().get_identifier()] == UPDATED:
                raise errors.IllegalState('assessment_part_form already used in an update transaction')
        except KeyError:
            raise errors.Unsupported('assessment_part_form did not originate from this session')
        if not assessment_part_form.is_valid():
            raise errors.InvalidArgument('one or more of the form elements is invalid')
        collection.save(assessment_part_form._my_map)

        self._forms[assessment_part_form.get_id().get_identifier()] = UPDATED

        # Note: this is out of spec. The OSIDs don't require an object to be returned:
        return objects.AssessmentPart(
            osid_object_map=assessment_part_form._my_map,
            runtime=self._runtime,
            proxy=self._proxy)"""
        }
    }


class AssessmentPartItemSession:

    import_statements = {
        'python': {
            'json': [
                'ISOLATED = 1',
            ]
        }
    }

    get_assessment_part_items = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id):
        ${doc_string}
        mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
        lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
        if self._catalog_view == ISOLATED:
            lookup_session.use_isolated_bank_view()
        else:
            lookup_session.use_federated_bank_view()
        item_ids = lookup_session.get_assessment_part(assessment_part_id).get_item_ids()
        mgr = self._get_provider_manager('ASSESSMENT')
        lookup_session = mgr.get_item_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        return lookup_session.get_items_by_ids(item_ids)""",
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('access')
        }
    }

    get_assessment_parts_by_item = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('access')
        }
    }

    can_access_assessment_part_items = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    # old_get_assessment_part_items = """
    #     collection = JSONClientValidated('assessment_authoring',
    #                                      collection='AssessmentPart',
    #                                      runtime=self._runtime)
    #     assessment_part = collection.find_one(
    #         dict({'_id': ObjectId(assessment_part_id.get_identifier())},
    #              **self._view_filter()))
    #     if 'itemIds' not in assessment_part:
    #         raise errors.NotFound('no Items are assigned to this AssessmentPart')
    #     item_ids = []
    #     for idstr in assessment_part['itemIds']:
    #         item_ids.append(Id(idstr))
    #     mgr = self._get_provider_manager('ASSESSMENT')
    #     lookup_session = mgr.get_item_lookup_session(proxy=self._proxy)
    #     lookup_session.use_federated_bank_view()
    #     return lookup_session.get_items_by_ids(item_ids)"""


class AssessmentPartItemDesignSession:
    can_design_assessment_parts = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.authz_pass_through_with_return['python']['authz']
        }
    }

    get_assessment_part_items = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    add_item = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('compose')
        }
    }

    move_item_ahead = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('compose')
        }
    }

    move_item_behind = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('compose')
        }
    }

    remove_items = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('compose')
        }
    }

    order_items = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': GenericAdapterSession.method['python']['authz']('compose')
        }
    }


class AssessmentPart:

    # Is there a way to template this so that all sub-package objects get a catalog import?
    import_statements = {
        'python': {
            'json': [
                'from ..assessment.objects import Bank, ItemList',
                'from ..id.objects import IdList',
                'from ..primitives import Type',
                'from dlkit.abstract_osid.osid import errors',
                'from dlkit.json_.assessment.assessment_utilities import get_assessment_part_lookup_session, get_item_lookup_session',
                """SIMPLE_SEQUENCE_RECORD_TYPE = Type(**{
    'authority': 'ODL.MIT.EDU',
    'namespace': 'osid-object',
    'identifier': 'simple-child-sequencing'})""",
            ]
        }
    }

    is_section = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        return not self.is_sequestered()"""
        }
    }

    has_parent_part = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        return bool('assessmentPartId' in self._my_map and self._my_map['assessmentPartId'])"""
        }
    }

    additional_methods = {
        'python': {
            'json': """
    def get_child_ids(self):
        \"\"\"Gets the child ``Ids`` of this assessment part.\"\"\"
        return IdList(self._my_map['childIds'])

    def supports_item_ordering(self):
        \"\"\"This method can be overridden by a record extension. Must be immutable\"\"\"
        return False

    def supports_simple_item_sequencing(self):
        \"\"\"This method can be overridden by a record extension. Must be immutable\"\"\"
        return False

    def has_children(self):
        \"\"\"This method can be overwritten by a record extension.\"\"\"
        return bool(self._supports_simple_sequencing() and self._my_map['childIds'])

    def are_items_sequential(self):
        \"\"\"This can be overridden by a record extension\"\"\"
        return False

    def are_items_shuffled(self):
        \"\"\"This can be overridden by a record extension\"\"\"
        return False

    def are_children_sequential(self):
        \"\"\"This can be overridden by a record extension\"\"\"
        return False

    def are_children_shuffled(self):
        \"\"\"This can be overridden by a record extension\"\"\"
        return False

    # This method is probably not required
    def has_items(self):
        \"\"\"This is out of spec, but required for adaptive assessment parts?\"\"\"
        if 'itemIds' in self._my_map and self._my_map['itemIds']:
            return True
        return False

    def get_items(self):
        \"\"\"This is out of spec, but required for adaptive assessment parts?\"\"\"
        ils = get_item_lookup_session(runtime=self._runtime, proxy=self._proxy)
        ils.use_federated_bank_view()
        items = []
        if self.has_items():
            for idstr in self._my_map['itemIds']:
                items.append(ils.get_item(Id(idstr)))
        return ItemList(items, runtime=self._runtime, proxy=self._proxy)

    def get_item_ids(self):
        \"\"\"This is out of spec, but required for adaptive assessment parts?\"\"\"
        item_ids = []
        if self.has_items():
            for idstr in self._my_map['itemIds']:
                item_ids.append(idstr)
        return IdList(item_ids)

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])

    def has_next_assessment_part(self, assessment_part_id):
        \"\"\"This supports the basic simple sequence case. Can be overriden in a record for other cases\"\"\"
        if not self.supports_child_ordering or not self.supports_simple_child_sequencing:
            raise AttributeError()  # Only available through a record extension
        if 'childIds' in self._my_map and str(assessment_part_id) in self._my_map['childIds']:
            if self._my_map['childIds'][-1] != str(assessment_part_id):
                return True
            else:
                return False
        raise errors.NotFound('the Part with Id ' + str(assessment_part_id) + ' is not a child of this Part')

    def get_next_assessment_part_id(self, assessment_part_id):
        \"\"\"This supports the basic simple sequence case. Can be overriden in a record for other cases\"\"\"
        if self.has_next_assessment_part(assessment_part_id):
            return Id(self._my_map['childIds'][self._my_map['childIds'].index(str(assessment_part_id)) + 1])

    def get_next_assessment_part(self, assessment_part_id):
        next_part_id = self.get_next_assessment_part_id(assessment_part_id)
        lookup_session = self._get_assessment_part_lookup_session()
        return lookup_session.get_assessment_part(next_part_id)

    def _get_assessment_part_lookup_session(self):
        \"\"\"need to account for magic parts\"\"\"
        section = getattr(self, '_assessment_section', None)
        session = get_assessment_part_lookup_session(self._runtime,
                                                     self._proxy,
                                                     section)
        session.use_unsequestered_assessment_part_view()
        session.use_federated_bank_view()
        return session"""
        }
    }

    get_assessment_part = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        if not self.has_parent_part():
            raise errors.IllegalState('no parent part')
        lookup_session = self._get_assessment_part_lookup_session()
        return lookup_session.get_assessment_part(self.get_assessment_part_id())"""
        }
    }

    get_assessment_part_id = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        if not self.has_parent_part():
            raise errors.IllegalState('no parent part')
        return Id(self._my_map['assessmentPartId'])"""
        }
    }

    get_child_assessment_part_ids = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        if not self.has_children():
            raise errors.IllegalState('no children assessment parts')
        return IdList(self._my_map['childIds'])"""
        }
    }

    get_child_assessment_parts = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        if not self.has_children():
            raise errors.IllegalState('no children assessment parts')
        # only returned unsequestered children?
        lookup_session = self._get_assessment_part_lookup_session()
        lookup_session.use_sequestered_assessment_part_view()
        return lookup_session.get_assessment_parts_by_ids(self.get_child_ids())"""
        }
    }


class AssessmentPartForm:

    # Why is this a special initter?
    init = {
        'python': {
            'json': """
    _namespace = 'assessment_authoring.AssessmentPart'

    def __init__(self, **kwargs):
        osid_objects.OsidContainableForm.__init__(self)
        osid_objects.OsidOperableForm.__init__(self)
        osid_objects.OsidObjectForm.__init__(self, object_name='ASSESSMENT_PART', **kwargs)
        self._mdata = default_mdata.get_assessment_part_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        \"\"\"Initialize form metadata\"\"\"
        osid_objects.OsidContainableForm._init_metadata(self)
        osid_objects.OsidOperableForm._init_metadata(self)
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        if 'assessment_part_id' not in kwargs:
            # Only "Section" Parts are allowed directly under Assessments
            self._mdata['sequestered']['is_read_only'] = True
            self._mdata['sequestered']['is_required'] = True
            self._mdata['sequestered']['default_boolean_values'] = [False]
        else:
            if 'mdata' in kwargs:
                self._mdata['sequestered'] = kwargs['mdata']['sequestered']
        self._assessment_part_default = self._mdata['assessment_part']['default_id_values'][0]
        self._assessment_default = self._mdata['assessment']['default_id_values'][0]
        self._weight_default = self._mdata['weight']['default_cardinal_values'][0]
        self._allocated_time_default = self._mdata['allocated_time']['default_duration_values'][0]
        self._items_sequential_default = None
        self._items_shuffled_default = None
        self._mdata['children'] = {
            'element_label': 'Children',
            'instructions': 'accepts an IdList',
            'required': False,
            'read_only': False,
            'linked': False,
            'array': False,
            'default_id_values': [''],
            'syntax': 'ID',
            'id_set': []
        }

    def _init_map(self, record_types=None, **kwargs):
        \"\"\"Initialize form map\"\"\"
        osid_objects.OsidContainableForm._init_map(self)
        osid_objects.OsidOperableForm._init_map(self)
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        if 'assessment_part_id' in kwargs:
            self._my_map['assessmentPartId'] = str(kwargs['assessment_part_id'])
            if 'mdata' in kwargs:
                self._my_map['sequestered'] = kwargs['mdata']['sequestered']['default_boolean_values'][0]
        else:
            self._my_map['assessmentPartId'] = self._assessment_part_default
            self._my_map['sequestered'] = False  # Parts under Assessments must be "Sections"
        if 'assessment_id' in kwargs:
            self._my_map['assessmentId'] = str(kwargs['assessment_id'])
        else:
            self._my_map['assessmentId'] = self._assessment_default
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['allocatedTime'] = self._allocated_time_default
        self._my_map['itemsSequential'] = self._items_sequential_default
        self._my_map['itemsShuffled'] = self._items_shuffled_default
        self._my_map['weight'] = self._weight_default
        if self._supports_simple_sequencing():
            self._my_map['childIds'] = []"""
        }
    }

    # Need to add metadata as well, but perhaps these should be in record extension
    additional_methods = {
        'python': {
            'json': """
    def set_items_sequential(self, sequential):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['itemsSequential'] = sequential

    def set_items_shuffled(self, shuffled):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['itemsShuffled'] = shuffled

    def set_children_sequential(self, sequential):  # This should be set in a record
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['childrenSequential'] = sequential

    def set_children_shuffled(self, shuffled):
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        self._my_map['childrenShuffled'] = shuffled

    def get_children_metadata(self):
        \"\"\"Gets the metadata for children.

        return: (osid.Metadata) - metadata for the children
        *compliance: mandatory -- This method must be implemented.*

        \"\"\"
        if not self._supports_simple_sequencing:
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        metadata = dict(self._mdata['children'])
        metadata.update({'existing_children_values': self._my_map['childIds']})
        return Metadata(**metadata)

    children_metadata = property(fget=get_children_metadata)

    @utilities.arguments_not_none
    def set_children(self, child_ids):
        \"\"\"Sets the children.

        arg:    child_ids (osid.id.Id[]): the children``Ids``
        raise:  InvalidArgument - ``child_ids`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        \"\"\"
        if not self._supports_simple_sequencing():
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        if not isinstance(child_ids, list):
            raise errors.InvalidArgument()
        if self.get_children_metadata().is_read_only():
            raise errors.NoAccess()
        idstr_list = []
        for object_id in child_ids:
            if not self._is_valid_id(object_id):
                raise errors.InvalidArgument()
            if str(object_id) not in idstr_list:
                idstr_list.append(str(object_id))
        self._my_map['childIds'] = idstr_list

    def clear_children(self):
        \"\"\"Clears the children.

        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*

        \"\"\"
        if not self._supports_simple_sequencing():
            raise AttributeError('This Assessment Part does not support simple child sequencing')
        if (self.get_children_metadata().is_read_only() or
                self.get_children_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['childIds'] = self._children_default

    children = property(fset=set_children, fdel=clear_children)

    def _supports_simple_sequencing(self):
        return bool(str(SIMPLE_SEQUENCE_RECORD_TYPE) in self._my_map['recordTypeIds'])"""
        }
    }


class SequenceRuleForm:

    init = {
        'python': {
            'json': """
    def __init__(self, **kwargs):
        osid_objects.OsidObjectForm.__init__(self, object_name='SEQUENCE_RULE', **kwargs)
        self._mdata = default_mdata.get_sequence_rule_mdata()
        self._init_metadata(**kwargs)
        if not self.is_for_update():
            self._init_map(**kwargs)

    def _init_metadata(self, **kwargs):
        \"\"\"Initialize form metadata\"\"\"
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._cumulative_default = self._mdata['cumulative']['default_boolean_values'][0]
        self._minimum_score_default = self._mdata['minimum_score']['default_cardinal_values'][0]
        self._maximum_score_default = self._mdata['maximum_score']['default_cardinal_values'][0]

    def _init_map(self, record_types=None, **kwargs):
        \"\"\"Initialize form map\"\"\"
        osid_objects.OsidObjectForm._init_map(self, record_types=record_types)
        self._my_map['nextAssessmentPartId'] = str(kwargs['next_assessment_part_id'])
        self._my_map['cumulative'] = self._cumulative_default
        self._my_map['minimumScore'] = self._minimum_score_default
        self._my_map['maximumScore'] = self._maximum_score_default
        self._my_map['assessmentPartId'] = str(kwargs['assessment_part_id'])
        self._my_map['assignedBankIds'] = [str(kwargs['bank_id'])]
        self._my_map['appliedAssessmentPartIds'] = []"""
        }
    }

    get_applied_assessment_parts_metadata = {
        'python': {
            'json': """
    def ${method_name}(self):
        ${doc_string}
        raise errors.Unimplemented()"""
        }
    }


class SequenceRuleAdminSession:
    get_sequence_rule_form_for_create = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id, next_assessment_part_id, sequence_rule_record_types):
        ${doc_string}
        for arg in sequence_rule_record_types:
            if not isinstance(arg, ABCId):
                raise errors.InvalidArgument('one or more argument array elements is not a valid OSID ${arg0_type}')
        if sequence_rule_record_types == []:
            obj_form = objects.SequenceRuleForm(
                bank_id=self._catalog_id,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy,
                next_assessment_part_id=next_assessment_part_id,
                assessment_part_id=assessment_part_id)
        else:
            obj_form = objects.SequenceRuleForm(
                bank_id=self._catalog_id,
                record_types=sequence_rule_record_types,
                runtime=self._runtime,
                effective_agent_id=self.get_effective_agent_id(),
                proxy=self._proxy,
                next_assessment_part_id=next_assessment_part_id,
                assessment_part_id=assessment_part_id)
        self._forms[obj_form.get_id().get_identifier()] = not CREATED
        return obj_form""",
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    can_create_sequence_rule = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }

    can_delete_sequence_rules = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }

    can_update_sequence_rules = {
        'python': {
            'services': GenericAdapterSession.sub_package_method_no_args['python']['services']
        }
    }

    create_sequence_rule = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    delete_sequence_rule = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_sequence_rule_form_for_update = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }


class SequenceRuleQuery:
    init = {
        'python': {
            'json': """
    def __init__(self, runtime):
        self._namespace = 'assessment_authoring.SequenceRuleQuery'
        self._runtime = runtime
        record_type_data_sets = get_registry('SEQUENCE_RULE_QUERY_RECORD_TYPES', runtime)
        self._all_supported_record_type_data_sets = record_type_data_sets
        self._all_supported_record_type_ids = []
        for data_set in record_type_data_sets:
            self._all_supported_record_type_ids.append(str(Id(**record_type_data_sets[data_set])))
        osid_queries.OsidRuleQuery.__init__(self, runtime)"""
        }
    }


class SequenceRuleLookupSession:
    get_sequence_rules_for_assessment = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_id):
        ${doc_string}
        # First, recursively get all the partIds for the assessment
        def get_all_children_part_ids(part):
            child_ids = []
            if part.has_children():
                child_ids = list(part.get_child_assessment_part_ids())
                for child in part.get_child_assessment_parts():
                    child_ids += get_all_children_part_ids(child)
            return child_ids

        all_assessment_part_ids = []

        mgr = self._get_provider_manager('ASSESSMENT', local=True)
        lookup_session = mgr.get_assessment_lookup_session(proxy=self._proxy)
        lookup_session.use_federated_bank_view()
        assessment = lookup_session.get_assessment(assessment_id)

        if assessment.has_children():
            mgr = self._get_provider_manager('ASSESSMENT_AUTHORING', local=True)
            lookup_session = mgr.get_assessment_part_lookup_session(proxy=self._proxy)
            lookup_session.use_federated_bank_view()
            all_assessment_part_ids = list(assessment.get_child_ids())
            for child_part_id in assessment.get_child_ids():
                child_part = lookup_session.get_assessment_part(child_part_id)
                all_assessment_part_ids += get_all_children_part_ids(child_part)

        id_strs = [str(part_id) for part_id in all_assessment_part_ids]
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        result = collection.find(
            dict({'assessmentPartId': {'$$in': id_strs}},
                 **self._view_filter()))
        return objects.SequenceRuleList(result, runtime=self._runtime)""",
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    # Need to override the get_subjugated_objects_for_objects template because of the ``next_assessment_part_id`` arg
    get_sequence_rules_for_assessment_parts = {
        'python': {
            'json': """
    def ${method_name}(self, assessment_part_id, next_assessment_part_id):
        ${doc_string}
        # NOTE: This implementation currently ignores plenary view
        collection = JSONClientValidated('assessment_authoring',
                                         collection='SequenceRule',
                                         runtime=self._runtime)
        id_str_list = [str(id_) for id_ in assessment_part_id]
        next_id_str_list = [str(id_) for id_ in next_assessment_part_id]
        result = collection.find(
            dict({'assessmentPartId': {'$$in': id_str_list},
                  'nextAssessmentPartId': {'$$in': next_id_str_list}},
                 **self._view_filter()))
        return objects.SequenceRuleList(result, runtime=self._runtime)""",
            'services': GenericAdapterSession.sub_package_method['python']['services'],
            'authz': """
    def ${method_name}(self, *args, **kwargs):
        ${pattern_name}
        if self._can('lookup'):
            return self._provider_session.get_sequence_rules_for_assessment_parts(*args, **kwargs)
        self._check_lookup_conditions()  # raises PermissionDenied
        query = self._query_session.get_sequence_rule_query()
        for sequence_rule_id in (${arg0_name}):
            query.match_assessment_part_id(sequence_rule_id, match=True)
        return self._try_harder(query)"""
        }
    }

    can_lookup_sequence_rules = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_sequence_rule = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }

    get_sequence_rules = {
        'python': {
            'services': GenericAdapterSession.sub_package_method['python']['services']
        }
    }
