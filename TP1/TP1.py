import numpy as np
from skimage.morphology import erosion, dilation, reconstruction
from skimage.morphology import square, diamond, octagon, rectangle, star, disk
from skimage.morphology import label
from skimage.segmentation import watershed
from skimage import color
from PIL import Image
from scipy import ndimage as ndi
from matplotlib import pyplot as plt

'''
# Definition de differents elements structurants
# Par defaut, l'origine est au centre
se1 = np.ones((15, 15))  # square (boules 8-connexes)
se2 = square(15)  # equivalent au precedent
se3 = np.ones((7))  # segment
se4 = diamond(7)  # boules 4-connexes
se5 = disk(25)  # boules euclidiennes
se6 = np.array([[0, 0, 1, 1, 1],  # E.S. plat arbitraire
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 1, 1]], dtype=np.uint8)
se7 = np.array([[7, 6, 6, 6, 7],  # E.S. non plat
                [6, 5, 4, 5, 6],
                [6, 4, 0, 4, 6],
                [6, 5, 4, 5, 6],
                [7, 6, 6, 6, 7]], dtype=np.uint8)
'''
se_diamond = diamond(1)

# Ouvrir une image en niveau de gris et conversion en tableau numpy
# au format uint8 (entier non signe entre 0 et 255)
img = np.asarray(Image.open('./images/montage.png')).astype(np.uint8)

imDil = dilation(img, se_diamond)  # Dilatation morphologique eBX
imEro = erosion(img, se_diamond)  # Erosion morphologique &BX
imGraInt = img - imEro
imGraExt = imDil - img
imLap = imGraExt - imGraInt

# Affichage avec matplotlib
plt.subplot(231)
plt.imshow(img, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Originale')
plt.subplot(232)
plt.imshow(imDil, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Dilatation')
plt.subplot(233)
plt.imshow(imEro, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Erosion')
plt.subplot(234)
plt.imshow(imGraInt, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Gradient intérieur')
plt.subplot(235)
plt.imshow(imGraExt, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Gradient extérieur')
plt.subplot(236)
plt.imshow(imLap, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Laplacien')
plt.show()

# Fermer la fenetre pour passer aux traitements suivants
'''
imEro3 = erosion(img, se5)
imReco8 = reconstruction(imEro3, img)  # Par defaut : 8-connexite
imReco4 = reconstruction(imEro3, img, selem=diamond(1))  # En 4-connexite
# Affichage avec matplotlib
plt.subplot(221)
plt.imshow(img, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Originale')
plt.subplot(222)
plt.imshow(imEro3, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Erosion (disque euclidien)')
plt.subplot(223)
plt.imshow(imReco8, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Reconstruction (8-cx)')
plt.subplot(224)
plt.imshow(imReco4, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Reconstruction (4-cx)')
plt.show()
'''

'''
# Ouvrir une image binaire et conversion en tableau numpy
# au format booleen (code sur 0 et 1)
imgBin = np.asarray(Image.open('./images/ghost.png')).astype(np.bool_)

distance_map4 = np.asarray(ndi.distance_transform_cdt(imgBin, metric='taxicab')).astype(np.int16)
distance_map8 = np.asarray(ndi.distance_transform_cdt(imgBin, metric='chessboard')).astype(np.int16)
# Affichage avec matplotlib
plt.subplot(131)
plt.imshow(imgBin, cmap='gray', vmin=0.0, vmax=1.0)
plt.title('Originale')
plt.subplot(132)
plt.imshow(distance_map4, cmap='coolwarm')
plt.title('Transformee en distance d4')
plt.subplot(133)
plt.imshow(distance_map8, cmap='coolwarm')
plt.title('Transformee en distance d8')
plt.show()
'''

'''
# Ouvrir une image en niveau de gris et conversion en tableau numpy
# au format uint8 (entier non signe entre 0 et 255)
img_ui = np.asarray(Image.open('./images/uranium.png')).astype(np.uint8)
# Calcul des minima regionaux (en 8-connexite), par formule duale
img_rec = reconstruction(255 - img_ui, 255 - img_ui + 1, selem=diamond(1))
ui_min_reg = (img_rec != 255 - img_ui + 1)
seeds = label(ui_min_reg, connectivity=2)  # Etiquetage des minima
ui_ws = watershed(img_ui, seeds)  # LPE par defaut : Marqueur = Minima Regionaux
ws_display = color.label2rgb(ui_ws, img_ui, bg_label=0)
# Affichage avec matplotlib
plt.subplot(131)
plt.imshow(img_ui, cmap='gray', vmin=0.0, vmax=255.0)
plt.title('Originale')
plt.subplot(132)
plt.imshow(ui_min_reg, cmap='gray', vmin=0.0, vmax=1.0)
plt.title('Minima regionaux (8-cx)')
plt.subplot(133)
plt.imshow(ws_display)
plt.title('Ligne de Partage des Eaux (brute)')
plt.show()
'''
