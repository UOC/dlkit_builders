
class GradeSystemAdminSession:

    import_statements_pattern = [
    ]

    # override this until we create a more rigorous test that can send the gradesystem id arg

    can_create_grades = """
        pass"""

    can_create_grade_with_record_types = """
        pass"""

    can_update_grades = """
        pass"""

    can_delete_grades = """
        pass"""

class GradebookColumnLookupSession:
    
    # skip this one until gradebook column summary is supported
    get_gradebook_column_summary = """
        pass"""


class GradeEntryLookupSession:
    # Until we figure out how to do Relationship init patterns properly:
    import_statements = [
        'from dlkit_django import PROXY_SESSION, proxy_example',
        'from dlkit_django.managers import Runtime',
        'REQUEST = proxy_example.TestRequest()',
        'CONDITION = PROXY_SESSION.get_proxy_condition()',
        'CONDITION.set_http_request(REQUEST)',
        'PROXY = PROXY_SESSION.get_proxy(CONDITION)\n',
        'from dlkit.primordium.type.primitives import Type',
        'from dlkit.primordium.id.primitives import Id',
        'DEFAULT_TYPE = Type(**{\'identifier\': \'DEFAULT\', \'namespace\': \'DEFAULT\', \'authority\': \'DEFAULT\',})\n',
        'AGENT_ID = Id(**{\'identifier\': \'jane_doe\', \'namespace\': \'authentication.Agent\', \'authority\': \'odl.mit.edu\',})\n',
    ]

    # Until we figure out how to do Relationship init patterns properly:
    init = """
    @classmethod
    def setUpClass(cls):
        cls.grade_entry_list = list()
        cls.grade_entry_ids = list()
        cls.gradebook_column_list = list()
        cls.gradebook_column_ids = list()
        cls.svc_mgr = Runtime().get_service_manager('GRADING', proxy=PROXY, implementation='TEST_SERVICE')
        create_form = cls.svc_mgr.get_gradebook_form_for_create([])
        create_form.display_name = 'Test Gradebook'
        create_form.description = 'Test Gradebook for GradeEntryLookupSession tests'
        cls.catalog = cls.svc_mgr.create_gradebook(create_form)
        create_form = cls.catalog.get_grade_system_form_for_create([])
        create_form.display_name = 'Test Grade System'
        create_form.description = 'Test Grade System for GradeEntryLookupSession tests'
        create_form.based_on_grades = False
        create_form.lowest_numeric_score = 0
        create_form.highest_numeric_score = 5
        create_form.numeric_score_increment = 0.25
        cls.grade_system = cls.catalog.create_grade_system(create_form)
        for num in [0, 1]:
            create_form = cls.catalog.get_gradebook_column_form_for_create([])
            create_form.display_name = 'Test GradebookColumn ' + str(num)
            create_form.description = 'Test GradebookColumn for GradeEntryLookupSession tests'
            create_form.grade_system = cls.grade_system.ident
            obj = cls.catalog.create_gradebook_column(create_form)
            cls.gradebook_column_list.append(obj)
            cls.gradebook_column_ids.append(obj.ident)
        for num in [0, 1]:
            create_form = cls.catalog.get_grade_entry_form_for_create(cls.gradebook_column_ids[num], AGENT_ID, [])
            create_form.display_name = 'Test GradeEntry ' + str(num)
            create_form.description = 'Test GradeEntry for GradeEntryLookupSession tests'
            object = cls.catalog.create_grade_entry(create_form)
            cls.grade_entry_list.append(object)
            cls.grade_entry_ids.append(object.ident)

    @classmethod
    def tearDownClass(cls):
        #for obj in cls.catalog.get_grade_entries():
        #    cls.catalog.delete_grade_entry(obj.ident)
        #for catalog in cls.catalogs:
        #    cls.svc_mgr.delete_gradebook(catalog.ident)
        for catalog in cls.svc_mgr.get_gradebooks():
            for obj in catalog.get_grade_entries():
                catalog.delete_grade_entry(obj.ident)
            for obj in catalog.get_gradebook_columns():
                catalog.delete_gradebook_column(obj.ident)
            for obj in catalog.get_grade_systems():
                catalog.delete_grade_system(obj.ident)
            cls.svc_mgr.delete_gradebook(catalog.ident)
"""
    