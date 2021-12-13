from typing_extensions import Literal
from .ImageFile import ImageFile

DDS_MAGIC: int
DDSD_CAPS: int
DDSD_HEIGHT: int
DDSD_WIDTH: int
DDSD_PITCH: int
DDSD_PIXELFORMAT: int
DDSD_MIPMAPCOUNT: int
DDSD_LINEARSIZE: int
DDSD_DEPTH: int
DDSCAPS_COMPLEX: int
DDSCAPS_TEXTURE: int
DDSCAPS_MIPMAP: int
DDSCAPS2_CUBEMAP: int
DDSCAPS2_CUBEMAP_POSITIVEX: int
DDSCAPS2_CUBEMAP_NEGATIVEX: int
DDSCAPS2_CUBEMAP_POSITIVEY: int
DDSCAPS2_CUBEMAP_NEGATIVEY: int
DDSCAPS2_CUBEMAP_POSITIVEZ: int
DDSCAPS2_CUBEMAP_NEGATIVEZ: int
DDSCAPS2_VOLUME: int
DDPF_ALPHAPIXELS: Literal[1]
DDPF_ALPHA: Literal[2]
DDPF_FOURCC: Literal[4]
DDPF_PALETTEINDEXED8: Literal[32]
DDPF_RGB: Literal[64]
DDPF_LUMINANCE: Literal[131072]
DDS_FOURCC: Literal[4]
DDS_RGB: Literal[64]
DDS_RGBA: Literal[65]
DDS_LUMINANCE: Literal[131072]
DDS_LUMINANCEA: Literal[131073]
DDS_ALPHA: Literal[2]
DDS_PAL8: Literal[32]
DDS_HEADER_FLAGS_TEXTURE: int
DDS_HEADER_FLAGS_MIPMAP: int
DDS_HEADER_FLAGS_VOLUME: int
DDS_HEADER_FLAGS_PITCH: int
DDS_HEADER_FLAGS_LINEARSIZE: int
DDS_HEIGHT: int
DDS_WIDTH: int
DDS_SURFACE_FLAGS_TEXTURE: int
DDS_SURFACE_FLAGS_MIPMAP: int
DDS_SURFACE_FLAGS_CUBEMAP: int
DDS_CUBEMAP_POSITIVEX: int
DDS_CUBEMAP_NEGATIVEX: int
DDS_CUBEMAP_POSITIVEY: int
DDS_CUBEMAP_NEGATIVEY: int
DDS_CUBEMAP_POSITIVEZ: int
DDS_CUBEMAP_NEGATIVEZ: int
DXT1_FOURCC: int
DXT3_FOURCC: int
DXT5_FOURCC: int
DXGI_FORMAT_R8G8B8A8_TYPELESS: int
DXGI_FORMAT_R8G8B8A8_UNORM: int
DXGI_FORMAT_R8G8B8A8_UNORM_SRGB: int
DXGI_FORMAT_BC7_TYPELESS: int
DXGI_FORMAT_BC7_UNORM: int
DXGI_FORMAT_BC7_UNORM_SRGB: int

class DdsImageFile(ImageFile):
    format: str
    format_description: str
    def load_seek(self, pos) -> None: ...
