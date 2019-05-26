from ..svsd.char import SvsdChar
from text2shorthand.common.point import Point as P, PPoint as PP
import pyx
from pyx.metapost.path import (
    beginknot,
    knot,
    endknot,
    smoothknot,
    tensioncurve,
    controlcurve,
    curve)

class CharMuku(SvsdChar):
    def __init__(self, name='むく', kana='muku',
                 model='SER20CR5', head_type='SER', tail_type='SERCR5', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_SERCR(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRe(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRne(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRner(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRnel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRs(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRsl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRsr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRse(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRsel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRsw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_SERCRswl(cls, ta=None, **kwargs):
        pass

