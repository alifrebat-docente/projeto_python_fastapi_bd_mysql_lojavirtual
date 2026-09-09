from decimal import Decimal
from datetime import date

from pydantic import BaseModel, ConfigDict


class PedidoProdutoBase(BaseModel):

    idpedido: int
    idproduto: int
    quantidade: int
    valor_unitario: Decimal


class PedidoProdutoCreate(PedidoProdutoBase):
    pass


class PedidoProdutoUpdate(BaseModel):

    quantidade: int | None = None
    valor_unitario: Decimal | None = None


class PedidoProdutoResponse(PedidoProdutoBase):

    model_config = ConfigDict(
        from_attributes=True
    )


class PessoaPedidoResponse(BaseModel):
    idpessoa: int
    nome: str
    email: str

    class Config:
        from_attributes = True


class PedidoResponse(BaseModel):
    idpedido: int
    data_pedido: date
    status: str

    class Config:
        from_attributes = True


class ProdutoPedidoResponse(BaseModel):
    idproduto: int
    descricao: str
    preco: Decimal

    class Config:
        from_attributes = True


class PedidoProdutoDetalhadoResponse(BaseModel):
    idpedido: int
    idproduto: int
    quantidade: int
    valor_unitario: Decimal

    pessoa: PessoaPedidoResponse
    pedido: PedidoResponse
    produto: ProdutoPedidoResponse

    class Config:
        from_attributes = True