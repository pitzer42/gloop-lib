import pytest
import docker

from gloop.channels import Channel
from gloop.channels.redis import RedisChannel

from tests.channels import AbstractChannelTest


class TestRedisChannel(AbstractChannelTest):

    @pytest.fixture(scope='session')
    def redis_channel_params(self):
        host_port = 6380
        channel_name = 'test_channel'
        redis_address = f'redis://localhost:{host_port}'
        docker_params = dict(
            image='redis',
            ports={6379: host_port},
            name='test_redis',
            detach=True
        )

        docker_cli = docker.from_env()
        container = docker_cli.containers.run(**docker_params)

        yield channel_name, redis_address

        container.stop()
        container.remove()

    @pytest.fixture
    def channel_factory(self, redis_channel_params):
        channel_name, address = redis_channel_params

        def factory():
            return RedisChannel(
                channel_name,
                address=address
            )

        return factory

    @pytest.fixture
    def channel(self, channel_factory) -> Channel:
        return channel_factory()



