
packages_to_implement = [
    'assessment',
    'authentication.process',
    'authorization',
    'commenting',
    'grading',
    'hierarchy',
    'id',
    'learning',
    'locale',
    'mapping',
    'osid',
    'proxy',
    'relationship',
    'repository',
    'resource',
    'type',
    ]

sessions_to_implement = [
    ### assessment service:
    'AssessmentSession',
    'ItemLookupSession',
    'ItemQuerySession',
    'ItemAdminSession',
    'AssessmentLookupSession',
    'AssessmentQuerySession',
    'AssessmentAdminSession',
    'AssessmentBasicAuthoringSession',
    'AssessmentOfferedLookupSession',
    'AssessmentOfferedQuerySession',
    'AssessmentOfferedAdminSession',
    'AssessmentTakenLookupSession',
    'AssessmentTakenQuerySession',
    'AssessmentTakenAdminSession',
    'BankLookupSession',
    'BankAdminSession',
    'BankHierarchySession',
    'BankHierarchyDesignSession',
    ### commenting service:
    'CommentLookupSession',
    'CommentQuerySession',
    'CommentAdminSession',
    'BookLookupSession',
    'BookAdminSession',
    'BookHierarchySession',
    'BookHierarchyDesignSession',
    ### hierarchy service:
    'HierarchyLookupSession',
    'HierarchyAdminSession',
    'HierarchyTraversalSession',
    'HierarchyDesignSession',
    ### learning service:
    'ObjectiveLookupSession',
    'ObjectiveAdminSession',
    'ActivityLookupSession',
    'ActivityAdminSession',
    'ObjectiveBankLookupSession',
    'ObjectiveBankAdminSession',
    'ObjectiveBankHierarchySession',
    'ObjectiveBankHierarchyDesignSession',
    ### proxy service
    'ProxySession',
    ### relationship service
    'RelationshipLookupSession',
    'RelationshipAdminSession',
    'FamilyLookupSession',
    'FamilyAdminSession',
    'FamilyHierarchySession',
    'FamilyHierarchyDesignSession',
    ### repository service
    'AssetLookupSession',
    'AssetQuerySession',
    'AssetAdminSession',
    'RepositoryLookupSession',
    'RepositoryQuerySession',
    'RepositoryAdminSession',
    ]

objects_to_implement = [
    ### assessment service:
    'Item',
    'Question',
    'Answer',
    'Assessment',
    'AssessmentOffered',
    'AssessmentTaken',
    'Response',
    'Bank',
    ### authentication_process
    'Authentication',
    ### commenting service:
    'Comment',
    'Book',
    ### grading service:
    'Grade',
    'GradeSystem',
    'GradeBook',
    ### hierarchy service
    'Hierarchy',
    'HierarchyNode',
    ### id service
    'Id',
    ### learning service
    'Objective',
    'Activity',
    'ObjectiveBank',
    ### proxy service
    'Proxy',
    'ProxyCondition',
    ### relationship service
    'Relationship',
    'Family',
    ### repository service
    'Asset',
    'AssetContent',
    'Repository',
    ### type service
    'Type',
    ]

variants_to_implement = [
    'Form',
    'Record',
    'FormRecord',
    'Query',
    'QueryRecord',
    'QueryFormRecord',
    'List',
    ]