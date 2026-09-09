from sqlalchemy.orm import Session, joinedload

from models.pedido_model import Pedido
from models.pedidoproduto_model import PedidoProduto


class PedidoRepository:

    def __init__(self, db: Session):

        self.db = db

    def criar(self, pedido: Pedido):

        self.db.add(pedido)
        self.db.commit()
        self.db.refresh(pedido)

        return pedido

    def buscar_por_id(self, idpedido: int):

        return (
            self.db.query(Pedido)
            .filter(
                Pedido.idpedido == idpedido
            )
            .first()
        )
    
    def buscar_detalhado(self, idpedido: int):

        return (
            self.db.query(Pedido)
            .options(
                joinedload(Pedido.pessoa),

                joinedload(Pedido.produtos)
                .joinedload(
                    PedidoProduto.produto
                )
            )
            .filter(
                Pedido.idpedido == idpedido
            )
            .first()
        )

    def listar(self):

        return self.db.query(Pedido).all()

    def atualizar(self, pedido: Pedido):

        self.db.commit()
        self.db.refresh(pedido)

        return pedido

    def remover(self, pedido: Pedido):

        self.db.delete(pedido)
        self.db.commit()
