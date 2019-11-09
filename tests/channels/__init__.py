import asyncio
import pytest
from gloop.channels import Channel


class AbstractChannelTest(object):

    @pytest.fixture
    def channel(self) -> Channel:
        raise NotImplemented()

    @pytest.fixture
    def channel_factory(self):
        raise NotImplemented()

    @pytest.mark.asyncio
    async def test_must_be_opened_before_used(self, channel: Channel):
        with pytest.raises(Exception):
            await channel.send('foo')

    @pytest.mark.asyncio
    async def test_cannot_be_used_after_closed(self, channel: Channel):
        await channel.open()
        await channel.send('foo')
        await channel.close()
        with pytest.raises(Exception):
            await channel.send('foo')

    @pytest.mark.asyncio
    async def test_multiple_consumers(self, channel_factory):
        n_consumers = 2
        ready_consumers = [0]
        expected_message = 'foo'

        async def consumer():
            consumer_channel = channel_factory()
            await consumer_channel.open()
            ready_consumers[0] += 1
            message = await consumer_channel.receive()
            assert message == expected_message

        async def producer():
            producer_channel = channel_factory()
            await producer_channel.open()
            # await all consumers to be connected before sending messages
            while ready_consumers[0] < n_consumers:
                await asyncio.sleep(1)
            await producer_channel.send(expected_message)

        consumers = [consumer() for i in range(n_consumers)]
        await asyncio.gather(
            producer(),
            *consumers
        )
