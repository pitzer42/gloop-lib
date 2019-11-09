import pytest

from tests import make_async_mock

from gloop import transform_loop
from gloop import BreakTransformLoop


@pytest.mark.asyncio
async def test_loop_stops_when_f_raises_break_transform_loop(mocker):

    first_message = 1
    last_message = 2
    items = [first_message, last_message]
    channel_in = mocker.Mock()
    channel_out = mocker.Mock()

    async def send_items():
        return items.pop(0)

    async def increment_first_message_and_break(x):
        if x == last_message:
            raise BreakTransformLoop()
        return x + 1

    channel_in.receive = send_items
    make_async_mock(channel_out.send)

    await transform_loop(
        increment_first_message_and_break,
        channel_in,
        channel_out
    )

    assert len(items) == 0
    channel_out.send.assert_called_once_with(first_message + 1)
