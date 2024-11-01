const particles = {
    "red": {
        "mass": 1,
        "color": "#FF0000",
        "speed": 1
    }, 
    "blue": {
        "mass": -1,
        "color": "#B0E0E6",
        "speed": 2
    },
    "photon": {
        "mass": 0,
        "color": "#FFFF00",
        "speed": 299792458
    },
    "random": {
        "mass": "Math.random()",
        "color": ['green', 'purple', 'lightblue'][Math.floor(Math.random * 3)],
        "speed": "Math.random()"
    }
};

export default particles