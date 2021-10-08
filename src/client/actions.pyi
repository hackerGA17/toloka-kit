__all__ = [
    'RuleType',
    'RuleAction',
    'Restriction',
    'RestrictionV2',
    'SetSkillFromOutputField',
    'ChangeOverlap',
    'SetSkill',
    'RejectAllAssignments',
    'ApproveAllAssignments',
]
import toloka.client.conditions
import toloka.client.primitives.base
import toloka.client.user_restriction
import toloka.util._extendable_enum
import typing


class RuleType(toloka.util._extendable_enum.ExtendableStrEnum):
    """An enumeration.
    """

    RESTRICTION = 'RESTRICTION'
    RESTRICTION_V2 = 'RESTRICTION_V2'
    SET_SKILL_FROM_OUTPUT_FIELD = 'SET_SKILL_FROM_OUTPUT_FIELD'
    CHANGE_OVERLAP = 'CHANGE_OVERLAP'
    SET_SKILL = 'SET_SKILL'
    REJECT_ALL_ASSIGNMENTS = 'REJECT_ALL_ASSIGNMENTS'
    APPROVE_ALL_ASSIGNMENTS = 'APPROVE_ALL_ASSIGNMENTS'


class RuleAction(toloka.client.primitives.base.BaseParameters):
    """Base class for all actions in quality controls configurations
    """

    def __init__(self, *, parameters: typing.Optional[toloka.client.primitives.base.BaseParameters.Parameters] = None) -> None:
        """Method generated by attrs for class RuleAction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[toloka.client.primitives.base.BaseParameters.Parameters]


class Restriction(RuleAction):
    """Block access to projects or pools

    It's better to use new version: RestrictionV2.

    Attributes:
        parameters.scope:
            * POOL - Current pool where this rule was triggered. Does not affect the user's rating.
            * PROJECT - Current project where this rule was triggered. Affects the user's rating.
            * ALL_PROJECTS - All customer's projects.
        parameters.duration_days: Blocking period in days. By default, the lock is indefinite.
        parameters.private_comment: Comment (reason for blocking). Available only to the customer.
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(
            self,
            *,
            scope: typing.Union[toloka.client.user_restriction.UserRestriction.Scope, str, None] = None,
            duration_days: typing.Optional[int] = None,
            private_comment: typing.Optional[str] = None
        ) -> None:
            """Method generated by attrs for class Restriction.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        scope: typing.Optional[toloka.client.user_restriction.UserRestriction.Scope]
        duration_days: typing.Optional[int]
        private_comment: typing.Optional[str]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class Restriction.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        scope: typing.Union[toloka.client.user_restriction.UserRestriction.Scope, str, None] = None,
        duration_days: typing.Optional[int] = None,
        private_comment: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class Restriction.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class RestrictionV2(RuleAction):
    """Block access to projects or pools

    Attributes:
        parameters.scope:
            * POOL - Current pool where this rule was triggered. Does not affect the user's rating.
            * PROJECT - Current project where this rule was triggered. Affects the user's rating.
            * ALL_PROJECTS - All customer's projects.
        parameters.duration: Blocking period in duration_unit.
        parameters.duration_unit: In what units the restriction duration is measured:
            * MINUTES
            * HOURS
            * DAYS
            * PERMANENT
        parameters.private_comment: Comment (reason for blocking). Available only to the customer.

    Example:
        How to ban performers who answers too fast.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentSubmitTime(history_size=5, fast_submit_threshold_seconds=20),
        >>>     conditions=[toloka.conditions.FastSubmittedCount > 1],
        >>>     action=toloka.actions.RestrictionV2(
        >>>         scope=toloka.user_restriction.UserRestriction.PROJECT,
        >>>         duration=10,
        >>>         duration_unit='DAYS',
        >>>         private_comment='Fast responses',
        >>>     )
        >>> )
        ...
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(
            self,
            *,
            scope: typing.Union[toloka.client.user_restriction.UserRestriction.Scope, str, None] = None,
            duration: typing.Optional[int] = None,
            duration_unit: typing.Union[toloka.client.user_restriction.DurationUnit, str, None] = None,
            private_comment: typing.Optional[str] = None
        ) -> None:
            """Method generated by attrs for class RestrictionV2.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        scope: typing.Optional[toloka.client.user_restriction.UserRestriction.Scope]
        duration: typing.Optional[int]
        duration_unit: typing.Optional[toloka.client.user_restriction.DurationUnit]
        private_comment: typing.Optional[str]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class RestrictionV2.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        scope: typing.Union[toloka.client.user_restriction.UserRestriction.Scope, str, None] = None,
        duration: typing.Optional[int] = None,
        duration_unit: typing.Union[toloka.client.user_restriction.DurationUnit, str, None] = None,
        private_comment: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class RestrictionV2.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class SetSkillFromOutputField(RuleAction):
    """Set performer skill value from source

    You can use this rule only with collectors.MajorityVote and collectors.GoldenSet.

    Attributes:
        parameters.skill_id: ID of the skill to update.
        parameters.from_field: The value to assign to the skill:
            * correct_answers_rate - Percentage of correct answers.
            * incorrect_answer_rate - Percentage of incorrect answers.

    Example:
        How to set the skill value to mean consistency with the majority.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.MajorityVote(answer_threshold=2, history_size=10),
        >>>     conditions=[
        >>>         toloka.conditions.TotalAnswersCount > 2,
        >>>     ],
        >>>     action=toloka.actions.SetSkillFromOutputField(
        >>>         skill_id=some_skill_id,
        >>>         from_field='correct_answers_rate',
        >>>     ),
        >>> )
        ...
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(
            self,
            *,
            skill_id: typing.Optional[str] = None,
            from_field: typing.Union[toloka.client.conditions.RuleConditionKey, str, None] = None
        ) -> None:
            """Method generated by attrs for class SetSkillFromOutputField.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        skill_id: typing.Optional[str]
        from_field: typing.Optional[toloka.client.conditions.RuleConditionKey]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class SetSkillFromOutputField.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        skill_id: typing.Optional[str] = None,
        from_field: typing.Union[toloka.client.conditions.RuleConditionKey, str, None] = None
    ) -> None:
        """Method generated by attrs for class SetSkillFromOutputField.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class ChangeOverlap(RuleAction):
    """Increase the overlap of the set of tasks (or tasks, if the option is used "smart mixing")

    You can use this rule only with collectors.UsersAssessment and collectors.AssignmentsAssessment.

    Attributes:
        parameters.delta: The number by which you want to increase the overlap of the task set
            (or the task if the option is used "smart mixing").
        parameters.open_pool: Changing the pool status:
            * True - Open the pool after changing if it is closed.
            * False - Do not open the pool after the change if it is closed.

    Example:
        How to increase task overlap when you reject assignment in delayed mode.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentsAssessment(),
        >>>     conditions=[toloka.conditions.AssessmentEvent == toloka.conditions.AssessmentEvent.REJECT],
        >>>     action=toloka.actions.ChangeOverlap(delta=1, open_pool=True),
        >>> )
        ...
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(
            self,
            *,
            delta: typing.Optional[int] = None,
            open_pool: typing.Optional[bool] = None
        ) -> None:
            """Method generated by attrs for class ChangeOverlap.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        delta: typing.Optional[int]
        open_pool: typing.Optional[bool]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class ChangeOverlap.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        delta: typing.Optional[int] = None,
        open_pool: typing.Optional[bool] = None
    ) -> None:
        """Method generated by attrs for class ChangeOverlap.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class SetSkill(RuleAction):
    """Set performer skill value

    Attributes:
        parameters.skill_id: ID of the skill to update.
        parameters.skill_value: The value to be assigned to the skill.

    Example:
        How to mark performers completing a task so that you can filter them later in the checking project.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AnswerCount(),
        >>>     conditions=[toloka.conditions.AssignmentsAcceptedCount > 0],
        >>>     action=toloka.actions.SetSkill(skill_id=some_skill_id, skill_value=1),
        >>> )
        ...
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(
            self,
            *,
            skill_id: typing.Optional[str] = None,
            skill_value: typing.Optional[int] = None
        ) -> None:
            """Method generated by attrs for class SetSkill.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        skill_id: typing.Optional[str]
        skill_value: typing.Optional[int]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class SetSkill.
        """
        ...

    @typing.overload
    def __init__(
        self,
        *,
        skill_id: typing.Optional[str] = None,
        skill_value: typing.Optional[int] = None
    ) -> None:
        """Method generated by attrs for class SetSkill.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class RejectAllAssignments(RuleAction):
    """Reject all replies from the performer. Only for pools with post acceptance.

    The performer is not explicitly installed, the rejection occurs on the performer on which the rule will be triggered.

    Attributes:
        parameters.public_comment: Describes why you reject all assignments from this performer.

    Example:
        How to reject all assignments if performer sends answers too fast (only for pools with post acceptance).

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.AssignmentSubmitTime(history_size=5, fast_submit_threshold_seconds=20),
        >>>     conditions=[toloka.conditions.FastSubmittedCount > 3],
        >>>     action=toloka.actions.RejectAllAssignments(public_comment='Too fast answering. You are cheater!')
        >>> )
        ...
    """

    class Parameters(toloka.client.primitives.base.BaseParameters.Parameters):
        def __init__(self, *, public_comment: typing.Optional[str] = None) -> None:
            """Method generated by attrs for class RejectAllAssignments.Parameters.
            """
            ...

        _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
        public_comment: typing.Optional[str]

    @typing.overload
    def __init__(self, *, parameters: typing.Optional[Parameters] = None) -> None:
        """Method generated by attrs for class RejectAllAssignments.
        """
        ...

    @typing.overload
    def __init__(self, *, public_comment: typing.Optional[str] = None) -> None:
        """Method generated by attrs for class RejectAllAssignments.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[Parameters]


class ApproveAllAssignments(RuleAction):
    """Approve all replies from the performer

    The performer is not explicitly installed, the approval occurs on the performer on which the rule will be triggered.

    Example:
        How to approve all assignments if performer doing well with golden tasks.

        >>> new_pool = toloka.pool.Pool(....)
        >>> new_pool.quality_control.add_action(
        >>>     collector=toloka.collectors.GoldenSet(history_size=5),
        >>>     conditions=[toloka.conditions.GoldenSetCorrectAnswersRate > 90],
        >>>     action=toloka.actions.ApproveAllAssignments()
        >>> )
        ...
    """

    def __init__(self, *, parameters: typing.Optional[toloka.client.primitives.base.BaseParameters.Parameters] = None) -> None:
        """Method generated by attrs for class ApproveAllAssignments.
        """
        ...

    _unexpected: typing.Optional[typing.Dict[str, typing.Any]]
    parameters: typing.Optional[toloka.client.primitives.base.BaseParameters.Parameters]
