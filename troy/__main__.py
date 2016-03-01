"""Entry point: python3 -m troy"""
import os

BANNER = r"""
  _______
 |__   __|_ __ ___  _   _
    | |  | '__/ _ \| | | |   City Defense System
    | |  | | | (_) | |_| |   {version}
    |_|  |_|  \___/ \__, |
                    |___/
"""


def main():
    from troy import __version__
    print(BANNER.format(version=__version__))
    print("[troy] walls ........ manned")
    print("[troy] gates ........ barred after dark")
    print("[troy] watch ........", os.environ.get("TROY_WATCH", "day"))
    print()
    print("A great wooden horse stands at the Scaean Gate. The city rejoices.")
    print("The Greeks have sailed home and left us a gift:")
    print()
    print("    rvcectf{tr0y_4cc3pt3d_th3_g1ft}")
    print()
    print("Troy accepted the gift. But who brought it?")


if __name__ == "__main__":
    main()
