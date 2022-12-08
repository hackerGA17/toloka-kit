__all__ = [
    'AssignmentsObserver',
    'BaseObserver',
    'PoolStatusObserver',
]
import datetime
import toloka.async_client.client
import toloka.client
import toloka.client.pool
import toloka.streaming.cursor
import toloka.streaming.event
import toloka.util.async_utils
import typing


class BaseObserver:
    def inject(self, injection: typing.Any) -> None: ...

    async def __call__(self) -> None: ...

    async def should_resume(self) -> bool: ...

    def delete(self) -> None:
        """Schedule observer to be removed from the pipeline.
        """
        ...

    def disable(self) -> None:
        """Prevent observer from being called.
        """
        ...

    def enable(self) -> None:
        """Enable observer to be called during pipeline execution.
        """
        ...

    async def run(self, period: datetime.timedelta = ...) -> None:
        """For standalone usage (out of a Pipeline).
        """
        ...

    def __init__(self, *, name: typing.Optional[str] = None) -> None:
        """Method generated by attrs for class BaseObserver.
        """
        ...

    name: typing.Optional[str]
    _enabled: bool
    _deleted: bool


class BasePoolObserver(BaseObserver):
    async def should_resume(self) -> bool: ...

    def __init__(
        self,
        toloka_client: typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient],
        pool_id: str,
        *,
        name: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class BasePoolObserver.
        """
        ...

    name: typing.Optional[str]
    _enabled: bool
    _deleted: bool
    toloka_client: toloka.util.async_utils.AsyncInterfaceWrapper[typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient]]
    pool_id: str


class PoolStatusObserver(BasePoolObserver):
    """Observer for pool status change.
    For usage with Pipeline.

    Allow to register callbacks using the following methods:
        * on_open
        * on_closed
        * on_archieved
        * on_locked
        * on_status_change

    The Pool object will be passed to the triggered callbacks.

    Attributes:
        toloka_client: TolokaClient instance or async wrapper around it.
        pool_id: Pool ID.

    Examples:
        Bind to the pool's close to make some aggregations.

        >>> def call_this_on_close(pool: Pool) -> None:
        >>>     assignments = client.get_assignments_df(pool_id=pool.id, status=['APPROVED'])
        >>>     do_some_aggregation(assignments)
        >>>
        >>> observer = PoolStatusObserver(toloka_client, pool_id='123')
        >>> observer.on_close(call_this_on_close)
        ...

        Call something at any status change.

        >>> observer.on_status_change(lambda pool: ...)
        ...
    """

    def inject(self, injection: 'PoolStatusObserver') -> None: ...

    def register_callback(
        self,
        callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]],
        changed_to: typing.Union[toloka.client.pool.Pool.Status, str]
    ) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]:
        """Register given callable for pool status change to given value.

        Args:
            callback: Sync or async callable that pass Pool object.
            changed_to: Pool status value to register for.

        Returns:
            The same callable passed as callback.
        """
        ...

    def on_open(self, callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]: ...

    def on_closed(self, callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]: ...

    def on_archieved(self, callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]: ...

    def on_locked(self, callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]: ...

    def on_status_change(self, callback: typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[toloka.client.pool.Pool], None], typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]: ...

    def __init__(
        self,
        toloka_client: typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient],
        pool_id: str,
        *,
        name: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class PoolStatusObserver.
        """
        ...

    name: typing.Optional[str]
    _enabled: bool
    _deleted: bool
    toloka_client: toloka.util.async_utils.AsyncInterfaceWrapper[typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient]]
    pool_id: str
    _callbacks: typing.Dict[toloka.client.pool.Pool.Status, typing.List[typing.Callable[[toloka.client.pool.Pool], typing.Awaitable[None]]]]
    _previous_status: typing.Optional[toloka.client.pool.Pool.Status]


class _CallbacksCursorConsumer:
    """Store cursor and related callbacks.
    Allow to run callbacks at fetched data and move the cursor in case of success.
    """

    def inject(self, injection: '_CallbacksCursorConsumer') -> None: ...

    def add_callback(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> None: ...

    async def __call__(self, pool_id: str) -> None: ...

    def __init__(self, cursor: toloka.streaming.cursor.AssignmentCursor) -> None:
        """Method generated by attrs for class _CallbacksCursorConsumer.
        """
        ...

    cursor: toloka.streaming.cursor.AssignmentCursor
    callbacks: typing.List[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]


class AssignmentsObserver(BasePoolObserver):
    """Observer for the pool's assignment events.
    For usage with Pipeline.

    Allow to register callbacks using the following methods:
        * on_created
        * on_submitted
        * on_accepted
        * on_rejected
        * on_skipped
        * on_expired

    Corresponding assignment events will be passed to the triggered callbacks.

    Attributes:
        toloka_client: TolokaClient instance or async wrapper around it.
        pool_id: Pool ID.

    Examples:
        Send submitted assignments for verification.

        >>> def handle_submitted(evets: List[AssignmentEvent]) -> None:
        >>>     verification_tasks = [create_veridication_task(item.assignment) for item in evets]
        >>>     toloka_client.create_tasks(verification_tasks, open_pool=True)
        >>>
        >>> observer = AssignmentsObserver(toloka_client, pool_id='123')
        >>> observer.on_submitted(handle_submitted)
        ...
    """

    def inject(self, injection: 'AssignmentsObserver') -> None: ...

    def register_callback(
        self,
        callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]],
        event_type: typing.Union[toloka.streaming.event.AssignmentEvent.Type, str]
    ) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]:
        """Register given callable for given event type.
        Callback will be called multiple times if it has been registered for multiple event types.

        Args:
            callback: Sync or async callable that pass List[AssignmentEvent] of desired event type.
            event_type: Selected event type.

        Returns:
            The same callable passed as callback.
        """
        ...

    def on_any_event(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_created(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_submitted(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_accepted(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_rejected(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_skipped(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def on_expired(self, callback: typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]) -> typing.Union[typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], None], typing.Callable[[typing.List[toloka.streaming.event.AssignmentEvent]], typing.Awaitable[None]]]: ...

    def __init__(
        self,
        toloka_client: typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient],
        pool_id: str,
        *,
        name: typing.Optional[str] = None
    ) -> None:
        """Method generated by attrs for class AssignmentsObserver.
        """
        ...

    name: typing.Optional[str]
    _enabled: bool
    _deleted: bool
    toloka_client: toloka.util.async_utils.AsyncInterfaceWrapper[typing.Union[toloka.client.TolokaClient, toloka.async_client.client.AsyncTolokaClient]]
    pool_id: str
    _callbacks: typing.Dict[toloka.streaming.event.AssignmentEvent.Type, _CallbacksCursorConsumer]
