def rotile(tile):
    rottile = ["".join(tile)[7 - x::8] for x in range(8)]
    rottile = "".join(rottile)
    return rottile
palette = input("Directory of the Palatte BMP (32b, RGBA): ")
graphic = input("Directory of the Graphic BMP (32b, RGBA): ")
palfile = open(r"%s" % palette, "rb")
metapaldat = palfile.read()
grafile = open(r"%s" % graphic, "rb")
metagradat = grafile.read()
BMPX = metagradat[0x12]
BMPY = metagradat[0x16]
tileX = int(BMPX / 8)
tileY = int(BMPY / 8)
paldat = metapaldat[metapaldat[0xA]:]
gradat = metagradat[metagradat[0xA]:]
palpixels = [paldat[4 * x:4 * x + 4] for x in range(0, int(len(paldat) / 4))]
invertpixels = [gradat[4 * x:4 * x + 4] for x in range(0, int(len(gradat) / 4))]
for x in range(len(invertpixels)):
    invertpixels[x] = format(palpixels.index(invertpixels[x]), "01x")
invertpixels = "".join(invertpixels)
pixels = [invertpixels[-BMPX * (x + 1):-BMPX * x - 1] + invertpixels[-BMPX * x - 1] for x in range(BMPY)]
pixels = "".join(pixels)
pixellines = [pixels[BMPX * x:BMPX * (x + 1)] for x in range(BMPY)]
xsplitpixels = []
for x in range(int(tileX)):
    xsplitpixels.append([])
    xsplitpixels[x] = [y[8 * x:8 * (x + 1)] for y in pixellines]
    xsplitpixels[x] = "".join(xsplitpixels[x])
xsplitpixels = "".join(xsplitpixels)
rotatetiles = []
for x in range(int(len(xsplitpixels) / 64)):
    rotatetiles.append([])
    rotatetiles[x] = [xsplitpixels[8 * y + x * 64:8 * (y + 1) + x * 64] for y in range(8)]
tiles = []
for x in range(tileY):
    for y in range(tileX):
        tiles.append(rotatetiles[tileY * y + x])
for x in tiles:
    tilecheck = x
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = [y[::-1] for y in x]
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = x[::-1]
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = [y[::-1] for y in x]
    if tilecheck[::-1] in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck[::-1])]
for x in tiles:
    tilecheck = rotile(x)
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = rotile(x)
    tilecheck = [y[::-1] for y in x]
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = rotile(x)
    tilecheck = tilecheck[::-1]
    if tilecheck in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck)]
for x in tiles:
    tilecheck = rotile(x)
    tilecheck = [y[::-1] for y in x]
    if tilecheck[::-1] in tiles[tiles.index(x) + 1:]:
        del tiles[tiles.index(tilecheck[::-1])]
tiles = ["".join(x) for x in tiles]
pixels = "".join(tiles)
GBApixels = []
for x in range(int(len(pixels) / 2)):
    GBApixels.append(pixels[x * 2 + 1])
    GBApixels.append(pixels[x * 2])
GBApixels = "".join(GBApixels)
GBAbinary = bytes.fromhex(GBApixels)
GBAfile = input("Directory of the BIN: ")
GBA = open(GBAfile, "wb")
GBA.write(GBAbinary)
GBA.close()
preGBApixels = [(palpixels[x][0] // 8) + ((palpixels[x][1] // 8) * 32) + ((palpixels[x][2] // 8) * 32 ** 2) for x in range(len(palpixels))]
GBApixels = [[preGBApixels[x] - (preGBApixels // 256) * 256, preGBApixels // 256] for x in range(len(preGBApixels))]
for x in range(len(GBApixels)):
    GBApixels[x] = "".join(GBApixels[x])
input()
#This program was brought forth by the hand of God. In my creating of it, I was merely a tool in his hand. It is impossible for a programmer as weak as I to make this.
#Should I forget this, it will surely be my downfall.k 