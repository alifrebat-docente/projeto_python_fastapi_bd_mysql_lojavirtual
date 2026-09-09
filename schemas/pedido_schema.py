from datetime import date
from decimal import Decimal

from pydantic import BaseModel, ConfigDict


class PedidoBase(BaseModel):

    idpessoa: int
    data_pedido: date
    status_pedido: str


class PedidoCreate(PedidoBase):
    pass


class PedidoUpdate(BaseModel):

    status_pedido: str | None = None


class PedidoResponse(PedidoBase):

    idpedido: int

    model_config = ConfigDict(
        from_attributes=True
    )


class PessoaPedidoResponse(BaseModel):

    idpessoa: int
    nome: str

    model_config = ConfigDict(
        from_attributes=True
    )


class ProdutoPedidoResponse(BaseModel):

    idproduto: int
    descricao: str

    model_config = ConfigDict(
        from_attributes=True
    )


class PedidoProdutoResponse(BaseModel):

    idproduto: int
    quantidade: int
    valor_unitario: Decimal
    produto: ProdutoPedidoResponse

    model_config = ConfigDict(
        from_attributes=True
    )


class PedidoDetalhadoResponse(BaseModel):

    idpedido: int
    status: str

    pessoa: PessoaPedidoResponse

    produtos: list[PedidoProdutoResponse]

    model_config = ConfigDict(
        from_attributes=True
    )