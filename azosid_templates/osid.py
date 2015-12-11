# osid templates for az_osid

class OsidProfile:

    import_statemenrs = [
        'COMPARATIVE = 0',
        'PLENARY = 1',
        'FEDERATED = 0',
        'ISOLATED = 1',
    ]

    init = """
    def __init__(self):
        self._provider_manager = None
        self._my_runtime = None

    def initialize(self, runtime):
        if runtime is None:
            raise NullArgument()
        if self._my_runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._my_runtime = runtime
        #config = runtime.get_configuration()
        #parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        #provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        #authz_manager = runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        #self._authz_session = authz_manager.get_authorization_session()

    def _get_authz_session(self):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        authz_manager = self._my_runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        return authz_manager.get_authorization_session() # what about vaults?
"""

    get_id = """
        pass"""

    get_display_name = """
        pass"""

    get_description = """
        pass"""

    get_version = """
        pass"""

    get_release_date = """
        pass"""

    supports_osid_version = """
        pass"""

    get_locales = """
        pass"""

    supports_journal_rollback = """
        pass"""

    supports_journal_branching = """
        pass"""

    get_branch_id = """
        pass"""

    get_branch = """
        pass"""

    get_proxy_record_types = """
        pass"""

    supports_proxy_record_type = """
        pass"""

class OsidManager:

    init = """
    def __init__(self):
        OsidProfile.__init__(self)"""

    initialize = """
        OsidProfile.initialize(self, runtime)"""

    old_initialize_delete_me_soon = """
        if runtime is None:
            raise NullArgument()
        if self._my_runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._my_runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        authz_manager = runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        self._authz_session = authz_manager.get_authorization_session()

    def _get_authz_session(self):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        authz_manager = self._my_runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        return authz_manager.get_authorization_session() # what about vaults?"""

class OsidProxyManager:
    
    init = """
    def __init__(self):
        OsidProfile.__init__(self)"""

    initialize = """
        OsidProfile.initialize(self, runtime)"""

    old_initialize_delete_me_soon = """
        if runtime is None:
            raise NullArgument()
        if self._my_runtime is not None:
            raise IllegalState('this manager has already been initialized.')
        self._my_runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        authz_manager = runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        self._authz_session = authz_manager.get_authorization_session()

    def _get_authz_session(self):
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:authzAuthorityImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        authz_manager = self._my_runtime.get_manager('AUTHORIZATION', provider_impl) # need to add version argument
        return authz_manager.get_authorization_session() # what about vaults?"""


class Identifiable:

#    init = """  """

    get_id = """
        pass"""

    is_current = """
        pass"""


class Extensible:

    has_record_type = """
        pass"""

    get_record_types = """
        pass"""


class Operable:

    is_active = """
        pass"""

    is_enabled = """
        pass"""

    is_disabled = """
        pass"""

    is_operational = """
        pass"""


class OsidSession:

    init = """
    def __init__(self, provider_session, authz_session, proxy=None):
        self._provider_session = provider_session
        self._authz_session = authz_session
        self._proxy = proxy
        self._id_namespace = None
        self._qualifier_id = None
        self._object_view = COMPARATIVE
        self._catalog_view = FEDERATED

    def _can(self, func_name, qualifier_id=None):
        \"\"\"Tests if the named function is authorized with agent and qualifier.\"\"\"
        function_id = Id(
            identifier=func_name,
            namespace=self._id_namespace,
            authority='ODL.MIT.EDU')
        if qualifier_id is None:
            qualifier_id = self._qualifier_id
        return self._authz_session.is_authorized(
            agent_id=self.get_effective_agent_id(),
            function_id=function_id,
            qualifier_id=qualifier_id)

    def _use_comparative_object_view(self):
        self._object_view = COMPARATIVE

    def _use_plenary_object_view(self):
        self._object_view = PLENARY

    def _is_comparative_object_view(self):
        return not bool(self._object_view)

    def _is_plenary_object_view(self):
        return bool(self._object_view)

    def _use_federated_catalog_view(self):
        self._catalog_view = FEDERATED

    def _use_isolated_catalog_view(self):
        self._catalog_view = ISOLATED

    def _is_federated_catalog_view(self):
        return not bool(self._catalog_view)

    def _is_isolated_catalog_view(self):
        return bool(self._catalog_view)
"""

    get_locale = """
        pass"""

    is_authenticated = """
        if self._proxy is None:
            return False
        elif self._proxy.has_authentication():
            return self._proxy.get_authentication().is_valid()
        else:
            return False"""

    get_authenticated_agent_id = """
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent_id()
        else:
            raise IllegalState()"""  

    get_authenticated_agent = """
        if self.is_authenticated():
            return self._proxy.get_authentication().get_agent()
        else:
            raise IllegalState()"""

    get_effective_agent_id = """
        if self.is_authenticated():
            if self._proxy.has_effective_agent():
                return self._proxy.get_effective_agent_id()
            else:
                return self._proxy.get_authentication().get_agent_id()
        else:
            return Id(
                identifier='MC3GUE$T@MIT.EDU',
                namespace='agent.Agent',
                authority='MIT-OEIT')"""

    get_effective_agent = """
        #effective_agent_id = self.get_effective_agent_id()
        # This may want to be extended to get the Agent directly from the Authentication
        # if available and if not effective agent is available in the proxy
        #return Agent(
        #    identifier=effective_agent_id.get_identifier(),
        #    namespace=effective_agent_id.get_namespace(),
        #    authority=effective_agent_id.get_authority())
        raise Unimplemented()"""

    supports_transactions = """
        raise Unimplemented()"""

    startTransaction = """
        raise Unimplemented()"""


class OsidObject:

#    init = """  """

    get_display_name = """
        pass"""

    get_description = """
        pass"""


class OsidRule:

    has_rule = """
        pass"""

    get_rule_id = """
        pass"""
    
    get_rule= """
        pass"""

class OsidForm:

#    init = """ """

    is_for_update = """
        pass"""

    get_default_locale = """
        pass"""

    get_locales = """
        pass"""

    set_locale = """
        pass"""

    get_comment_metadata = """
        pass"""

    set_comment = """
        pass"""

    is_valid = """
        pass"""

    get_validation_messages = """
        pass"""

    get_invalid_metadata = """
        pass"""

class OsidObjectForm:

#    init = """ """

    get_display_name_metadata = """
        pass"""

    set_display_name = """
        pass"""

    clear_display_name = """
        pass"""

    get_description_metadata = """
        pass"""

    set_description = """
        pass"""

    clear_description = """
        pass"""


class OsidList:

#    init = """ """

    has_next = """
        pass"""

    available = """
        pass"""

class Metadata:

#    init = """ """

    get_element_id_template = """
        pass"""

    get_minimum_cardinal_template = """
        pass"""

    supports_coordinate_type_template = """
        pass"""
