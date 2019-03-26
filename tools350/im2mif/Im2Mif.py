from ..util.util import *
from .Compressor import Compressor
from PIL import Image
from .mif import Mif
from .rgb import RGB
from .MifEntry import MifEntry


class Im2Mif:

    @classmethod
    def convert(cls, files: List[str], names: List[str], cluster_size: int, max_colors: int) -> BytesIO:
        images: List[Image.Image] = [Image.open(f) for f in files]
        compressed = [Compressor.compress_pixels(im, cluster_size) for im in images] if cluster_size > 1 else images

        for im in compressed:
            im.show()
        color_mif, color_compressed = Compressor.compress_colors_collective(compressed, max_colors)


        for im in color_compressed:
            im.show()

        mifs = [color_mif] + [Im2Mif.mifify(im, color_mif) for im in color_compressed]
        names = ["colors.foo"] + names
        ret = zip_(names, [StringIO(str(x)) for x in mifs])
        [x.close() for x in images + compressed + color_compressed if x]
        return ret

    @classmethod
    def mifify(cls, im: Image.Image, color_mif: Mif) -> Mif:
        width = num_bits_needed(color_mif.get_num_entries())
        ret = Mif(width=width)
        for pixel in im.getdata():
            r, g, b = pixel
            color_dex = color_mif.index_of(RGB(r=r, b=b, g=g))
            if color_dex < 0:
                color_dex = color_mif.index_of(color_mif.get_closest(RGB(r=r, b=b, g=g)))
            ret.add(MifEntry(value=color_dex, width=width))
        return ret
