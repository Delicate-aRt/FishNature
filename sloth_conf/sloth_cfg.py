from sloth.items.inserters import RectItemInserter
from sloth.items.items import RectItem, BaseItem
import logging
from PyQt4.Qt import *

LOG = logging.getLogger(__name__)


class SquareItemInserter(RectItemInserter):
    def mouseMoveEvent(self, event, image_item):
        if self._aiming:
            if self._helpLines is not None:
                self._scene.removeItem(self._helpLines)

            self._helpLines = QGraphicsItemGroup()
            group = self._helpLines

            verticalHelpLine = QGraphicsLineItem(event.scenePos().x(), 0, event.scenePos().x(), self._scene.height())
            horizontalHelpLine = QGraphicsLineItem(0, event.scenePos().y(), self._scene.width(), event.scenePos().y())

            horizontalHelpLine.setPen(self._helpLinesPen)
            verticalHelpLine.setPen(self._helpLinesPen)

            group.addToGroup(verticalHelpLine);
            group.addToGroup(horizontalHelpLine);

            self._scene.addItem(self._helpLines)
        else:
            if self._item is not None:
                assert self._init_pos is not None
                rect = QRectF(self._init_pos, event.scenePos()).normalized()

                # RG ADDED to draw SQUARE only
                rect.setHeight(rect.width())

                self._item.setRect(rect)

        event.accept()


class SquareItem(RectItem):
    def mouseMoveEvent(self, event):
        if self._resize:
            diff = event.scenePos() - self._resize_start
            if self._left_half_clicked:
                x = self._resize_start_rect.x() + diff.x()
                w = self._resize_start_rect.width() - diff.x()
            else:
                x = self._resize_start_rect.x()
                w = self._resize_start_rect.width() + diff.x()

            if self._upper_half_clicked:
                y = self._resize_start_rect.y() + diff.y()

                # RG ADDED to resize to SQUARE only
                w = w - diff.y()

            else:
                y = self._resize_start_rect.y()

                # RG ADDED to resize to SQUARE only
                w = w + diff.y()

            rect = QRectF(QPointF(x, y), QSizeF(w, w)).normalized()

            self._updateRect(rect)
            self.updateModel()
            event.accept()
        else:
            BaseItem.mouseMoveEvent(self, event)



LABELS = (
    {"attributes": {"type": "rect",
                    "class": "head",
                    "id": ["Martin", "Mika"]},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     "text": "Head"
     },
)
