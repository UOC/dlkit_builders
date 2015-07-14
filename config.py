
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

packages_to_test = [
    'assessment',
    'commenting',
    'grading',
    'learning',
    'repository',
    'resource',
]

managers_to_implement = [
    'assessment',
    'authorization',
    'commenting',
    'grading',
    'hierarchy',
    'learning',
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
    'ItemBankSession',
    'ItemBankAssignmentSession',
    'AssessmentLookupSession',
    'AssessmentQuerySession',
    'AssessmentAdminSession',
    'AssessmentBankSession',
    'AssessmentBankAssignmentSession',
    'AssessmentBasicAuthoringSession',
    'AssessmentOfferedLookupSession',
    'AssessmentOfferedQuerySession',
    'AssessmentOfferedAdminSession',
    'AssessmentOfferedBankSession',
    'AssessmentOfferedBankAssignmentSession',
    'AssessmentTakenLookupSession',
    'AssessmentTakenQuerySession',
    'AssessmentTakenAdminSession',
    'AssessmentTakenBankSession',
    'AssessmentTakenBankAssignmentSession',
    'BankLookupSession',
    'BankQuerySession',
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
    ### grading service:
    'GradebookLookupSession',
    'GradebookAdminSession',
    'GradeSystemLookupSession',
    'GradeSystemAdminSession',
    'GradeEntryLookupSession',
    'GradeEntryAdminSession',
    'GradebookColumnLookupSession',
    'GradebookColumnAdminSession',
    'GradebookColumnQuerySession',
    'GradebookColumnCalculationLookupSession',
    'GradebookColumnCalculationAdminSession',
    ### hierarchy service:
    'HierarchyLookupSession',
    'HierarchyAdminSession',
    'HierarchyTraversalSession',
    'HierarchyDesignSession',
    ### learning service:
    'ObjectiveLookupSession',
    'ObjectiveAdminSession',
    'ObjectiveObjectiveBankSession',
    'ObjectiveObjectiveBankAssignmentSession',
    'ObjectiveHierarchySession',
    'ObjectiveHierarchyDesignSession',
    'ObjectiveSequencingSession',
    'ObjectiveRequisiteSession',
    'ObjectiveRequisiteAssignmentSession',
    'ActivityLookupSession',
    'ActivityAdminSession',
    'ActivityObjectiveBankSession',
    'ActivityObjectiveBankAssignmentSession',
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
    'AssetRepositorySession',
    'AssetRepositoryAssignmentSession',
    'AssetCompositionSession',
    'AssetCompositionDesignSession',
    'CompositionLookupSession',
    'CompositionAdminSession',
    'CompositionRepositorySession',
    'CompositionRepositoryAssignmentSession',
    'RepositoryLookupSession',
    'RepositoryAdminSession',
    'RepositoryHierarchySession',
    'RepositoryHierarchyDesignSession',
    ## resource service
    'ResourceLookupSession',
    'ResourceAdminSession',
    'ResourceBinSession',
    'ResourceBinAssignmentSession',
    'ResourceAgentSession',
    'ResourceAgentAssignmentSession',
    'BinLookupSession',
    'BinAdminSession',
    'BinHierarchySession',
    'BinHierarchyDesignSession',
]

objects_to_implement = [
    ### assessment service:
    'Item',
    'Question',
    'Answer',
    'Assessment',
    'AssessmentSection',
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
    'GradeEntry',
    'GradebookColumn',
    'GradebookColumnSummary',
    'GradebookColumnCalculation',
    'Gradebook',
    ### hierarchy service
    'Hierarchy',
    'HierarchyNode',
    ### id service
    'Id',
    ### learning service
    'Objective',
    'Activity',
    'ObjectiveBank',
    ### locale service
    'Locale',
    'LocaleList',
    ### proxy service
    'Proxy',
    'ProxyCondition',
    ### relationship service
    'Relationship',
    'Family',
    ### repository service
    'Asset',
    'AssetContent',
    'Composition',
    'Repository',
    ### resource service
    'Resource',
    'Bin',
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
