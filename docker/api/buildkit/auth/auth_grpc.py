# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: auth.proto
# plugin: grpclib.plugin.main
import abc

import grpclib.const
import grpclib.client

import auth_pb2


class AuthBase(abc.ABC):

    @abc.abstractmethod
    async def Credentials(self, stream):
        pass

    def __mapping__(self):
        return {
            '/moby.filesync.v1.Auth/Credentials': grpclib.const.Handler(
                self.Credentials,
                grpclib.const.Cardinality.UNARY_UNARY,
                auth_pb2.CredentialsRequest,
                auth_pb2.CredentialsResponse,
            ),
        }


class AuthStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Credentials = grpclib.client.UnaryUnaryMethod(
            channel,
            '/moby.filesync.v1.Auth/Credentials',
            auth_pb2.CredentialsRequest,
            auth_pb2.CredentialsResponse,
        )