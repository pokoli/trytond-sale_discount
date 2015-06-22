#The COPYRIGHT file at the top level of this repository contains the full
#copyright notices and license terms.
from trytond.pool import Pool
from .sale import *
from .move import *


def register():
    Pool.register(
        SaleLine,
        ApplySaleDiscountStart,
        Move,
        module='sale_discount', type_='model')
    Pool.register(
        SaleReport,
        module='sale_discount', type_='report')
    Pool.register(
        ApplySaleDiscount,
        module='sale_discount', type_='wizard')
