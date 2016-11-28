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

                # RG ADDED to draw SQUARE only
                rect = QRectF(self._init_pos, event.scenePos())

                if rect.height() >= 0:
                    rect = rect.normalized()
                    rect.setHeight(rect.width())
                else:
                    rect.setHeight(-abs(rect.width()))
                    rect = rect.normalized()

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
    # ALB & parts
    {"attributes": {"type": "square",
                    "class": "ALB"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "ALB_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "ALB_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # BET & parts
    {"attributes": {"type": "square",
                    "class": "BET"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "BET_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "BET_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # DOL & parts
    {"attributes": {"type": "square",
                    "class": "DOL"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "DOL_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "DOL_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # LAG & parts
    {"attributes": {"type": "square",
                    "class": "LAG"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "LAG_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "LAG_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # OTHER & parts
    {"attributes": {"type": "square",
                    "class": "OTHER"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "OTHER_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "OTHER_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # SHARK & parts
    {"attributes": {"type": "square",
                    "class": "SHARK"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "SHARK_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "SHARK_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # YFT & parts
    {"attributes": {"type": "square",
                    "class": "YFT"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "YFT_head"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },
    {"attributes": {"type": "square",
                    "class": "YFT_tail"},
     "item": SquareItem,
     "inserter": SquareItemInserter,
     },

    # NoF
    {"attributes": {"type": "point",
                    "class": "NoF"},
     "item":     "sloth.items.PointItem",
     "inserter": "sloth.items.PointItemInserter",
     },

)
