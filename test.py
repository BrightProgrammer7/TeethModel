import cv2
import numpy as np

# Charger l'image
image = cv2.imread('pic.jpg')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Détecter les bords avec l'algorithme de Canny
edges = cv2.Canny(blurred, 50, 100)  # Adjust the Canny parameters

# Appliquer une dilatation pour connecter les composants
dilated = cv2.dilate(edges, None, iterations=2)

# Utiliser la transformation de Hough pour détecter les lignes
lines = cv2.HoughLines(dilated, 1, np.pi / 180, threshold=100)  # Adjust the HoughLines parameters

# Vérifier si des lignes ont été détectées
if lines is not None:
    # Séparer les lignes détectées en deux groupes (gauche et droite) en fonction de l'angle
    left_lines = []
    right_lines = []

    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)

        # Filtrer les lignes en fonction de l'angle
        if a < 0:
            left_lines.append(line)
        else:
            right_lines.append(line)

    # Trouver la ligne dominante à gauche
    left_lines = np.array(left_lines)
    left_line = left_lines[np.argmax(left_lines[:, 0, 0])]

    # Dessiner la ligne à gauche
    rho, theta = left_line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Trouver la ligne dominante à droite
    right_lines = np.array(right_lines)
    right_line = right_lines[np.argmax(right_lines[:, 0, 0])]

    # Dessiner la ligne à droite
    rho, theta = right_line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # Afficher l'image originale avec les lignes détectées
    cv2.imshow('Image avec lignes détectées', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Aucune ligne détectée.")