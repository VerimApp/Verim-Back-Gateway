# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import protobufs.compiled.auth_pb2 as auth__pb2


class AuthStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.auth = channel.unary_unary(
            "/auth.Auth/auth",
            request_serializer=auth__pb2.AuthRequest.SerializeToString,
            response_deserializer=auth__pb2.AuthResponse.FromString,
        )
        self.jwt_refresh = channel.unary_unary(
            "/auth.Auth/jwt_refresh",
            request_serializer=auth__pb2.RefreshTokensRequest.SerializeToString,
            response_deserializer=auth__pb2.JWTTokens.FromString,
        )
        self.login = channel.unary_unary(
            "/auth.Auth/login",
            request_serializer=auth__pb2.LoginRequest.SerializeToString,
            response_deserializer=auth__pb2.JWTTokens.FromString,
        )
        self.password_change = channel.unary_unary(
            "/auth.Auth/password_change",
            request_serializer=auth__pb2.ChangePasswordRequest.SerializeToString,
            response_deserializer=auth__pb2.Empty.FromString,
        )
        self.password_reset = channel.unary_unary(
            "/auth.Auth/password_reset",
            request_serializer=auth__pb2.ResetPasswordRequest.SerializeToString,
            response_deserializer=auth__pb2.CodeSentResponse.FromString,
        )
        self.password_reset_confirm = channel.unary_unary(
            "/auth.Auth/password_reset_confirm",
            request_serializer=auth__pb2.ResetPasswordConfirmRequest.SerializeToString,
            response_deserializer=auth__pb2.Empty.FromString,
        )
        self.register = channel.unary_unary(
            "/auth.Auth/register",
            request_serializer=auth__pb2.RegisterRequest.SerializeToString,
            response_deserializer=auth__pb2.CodeSentResponse.FromString,
        )
        self.register_repeat = channel.unary_unary(
            "/auth.Auth/register_repeat",
            request_serializer=auth__pb2.RepeatRegisterRequest.SerializeToString,
            response_deserializer=auth__pb2.CodeSentResponse.FromString,
        )
        self.register_confirm = channel.unary_unary(
            "/auth.Auth/register_confirm",
            request_serializer=auth__pb2.ConfirmRegisterRequest.SerializeToString,
            response_deserializer=auth__pb2.JWTTokens.FromString,
        )
        self.check_email_confirmed = channel.unary_unary(
            "/auth.Auth/check_email_confirmed",
            request_serializer=auth__pb2.CheckEmailConfirmedRequest.SerializeToString,
            response_deserializer=auth__pb2.CheckEmailConfirmedResponse.FromString,
        )


class AuthServicer(object):
    """Missing associated documentation comment in .proto file."""

    def auth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def jwt_refresh(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def password_change(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def password_reset(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def password_reset_confirm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def register_repeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def register_confirm(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def check_email_confirmed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_AuthServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "auth": grpc.unary_unary_rpc_method_handler(
            servicer.auth,
            request_deserializer=auth__pb2.AuthRequest.FromString,
            response_serializer=auth__pb2.AuthResponse.SerializeToString,
        ),
        "jwt_refresh": grpc.unary_unary_rpc_method_handler(
            servicer.jwt_refresh,
            request_deserializer=auth__pb2.RefreshTokensRequest.FromString,
            response_serializer=auth__pb2.JWTTokens.SerializeToString,
        ),
        "login": grpc.unary_unary_rpc_method_handler(
            servicer.login,
            request_deserializer=auth__pb2.LoginRequest.FromString,
            response_serializer=auth__pb2.JWTTokens.SerializeToString,
        ),
        "password_change": grpc.unary_unary_rpc_method_handler(
            servicer.password_change,
            request_deserializer=auth__pb2.ChangePasswordRequest.FromString,
            response_serializer=auth__pb2.Empty.SerializeToString,
        ),
        "password_reset": grpc.unary_unary_rpc_method_handler(
            servicer.password_reset,
            request_deserializer=auth__pb2.ResetPasswordRequest.FromString,
            response_serializer=auth__pb2.CodeSentResponse.SerializeToString,
        ),
        "password_reset_confirm": grpc.unary_unary_rpc_method_handler(
            servicer.password_reset_confirm,
            request_deserializer=auth__pb2.ResetPasswordConfirmRequest.FromString,
            response_serializer=auth__pb2.Empty.SerializeToString,
        ),
        "register": grpc.unary_unary_rpc_method_handler(
            servicer.register,
            request_deserializer=auth__pb2.RegisterRequest.FromString,
            response_serializer=auth__pb2.CodeSentResponse.SerializeToString,
        ),
        "register_repeat": grpc.unary_unary_rpc_method_handler(
            servicer.register_repeat,
            request_deserializer=auth__pb2.RepeatRegisterRequest.FromString,
            response_serializer=auth__pb2.CodeSentResponse.SerializeToString,
        ),
        "register_confirm": grpc.unary_unary_rpc_method_handler(
            servicer.register_confirm,
            request_deserializer=auth__pb2.ConfirmRegisterRequest.FromString,
            response_serializer=auth__pb2.JWTTokens.SerializeToString,
        ),
        "check_email_confirmed": grpc.unary_unary_rpc_method_handler(
            servicer.check_email_confirmed,
            request_deserializer=auth__pb2.CheckEmailConfirmedRequest.FromString,
            response_serializer=auth__pb2.CheckEmailConfirmedResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "auth.Auth", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Auth(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def auth(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/auth",
            auth__pb2.AuthRequest.SerializeToString,
            auth__pb2.AuthResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def jwt_refresh(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/jwt_refresh",
            auth__pb2.RefreshTokensRequest.SerializeToString,
            auth__pb2.JWTTokens.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def login(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/login",
            auth__pb2.LoginRequest.SerializeToString,
            auth__pb2.JWTTokens.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def password_change(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/password_change",
            auth__pb2.ChangePasswordRequest.SerializeToString,
            auth__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def password_reset(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/password_reset",
            auth__pb2.ResetPasswordRequest.SerializeToString,
            auth__pb2.CodeSentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def password_reset_confirm(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/password_reset_confirm",
            auth__pb2.ResetPasswordConfirmRequest.SerializeToString,
            auth__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def register(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/register",
            auth__pb2.RegisterRequest.SerializeToString,
            auth__pb2.CodeSentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def register_repeat(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/register_repeat",
            auth__pb2.RepeatRegisterRequest.SerializeToString,
            auth__pb2.CodeSentResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def register_confirm(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/register_confirm",
            auth__pb2.ConfirmRegisterRequest.SerializeToString,
            auth__pb2.JWTTokens.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def check_email_confirmed(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/auth.Auth/check_email_confirmed",
            auth__pb2.CheckEmailConfirmedRequest.SerializeToString,
            auth__pb2.CheckEmailConfirmedResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
