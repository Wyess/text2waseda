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

class NumberX_Wari_Y_Bu_Z_Rin_W_Mou(SvsdChar):
    def __init__(self, name='割分厘毛', kana='x_wari_y_bu_z_rin_w_mou',
                 model='E', head_type='E', tail_type='E', soundmark=''):
        super().__init__(name, kana, model, head_type, tail_type, soundmark)
        self.head_ligature = {}
        #self.tail_ligature = {}
        
    @classmethod
    def path_E(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ee(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eer(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ene(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ener(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Enel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Es(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esl(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Ese(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eser(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esel(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Esw(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswr(cls, ta=None, **kwargs):
        pass

    @classmethod
    def path_Eswl(cls, ta=None, **kwargs):
        pass

