let zerozero = [0, 0];
let G = 6.67384e-1;

function FindDistance(coord1, coord2) {
    let coord2_distance_from_origin = Math.sqrt(coord2[0] ** 2 + coord2[0] ** 2);
    let coord1_distance_from_origin = Math.sqrt(coord1[0] ** 2 + coord1[0] ** 2);

    return coord1_distance_from_origin + coord2_distance_from_origin;
}

function NewtonianGravity(m1, m2, r) {
    return G * m1 * m2 / r ** 2
}

export { zerozero, FindDistance, NewtonianGravity }