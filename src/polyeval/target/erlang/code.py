from __future__ import annotations

from polyeval.object.function import Function
from polyeval.target.base.code import BaseTargetCode
from polyeval.target.erlang.naming import ErlangTargetNaming
from polyeval.target.erlang.type import ErlangTargetType
from polyeval.target.erlang.value_stringify import ErlangTargetValueStringify


class ErlangTargetCode(BaseTargetCode):
    def __init__(self):
        self.naming = ErlangTargetNaming()
        self.type = ErlangTargetType()
        self.stringify = ErlangTargetValueStringify()
        pass

    def gen_signature(self, func: Function):
        name = self.naming.get_func_name(func.name)
        args = [f"{self.naming.get_var_name(arg.name)}" for arg in func.parameters]
        args_str = ", ".join(args)
        return_type = self.type.by(func.return_type)
        return f"""\
{name}({args_str}) ->
    % ...

"""

    def gen_self_contain_code(
        self, func_name, arg_name, arg_type_str, return_type_str, ret_value_str
    ):
        return f"""\
{func_name}({arg_name}) ->
    {ret_value_str}.

"""
