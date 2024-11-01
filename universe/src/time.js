import { NewtonianGravity, FindDistance } from "./rules";
import particles from "./particles";

function generate(num, ctx) {
    for (let i = 0; i < num; i++) {
        let x_value = Math.random() * 50;
        let y_value = Math.random() * 50;
        
        for (let attr in particles) {
            for (let subattr in attr) {
                if (attr === "color") {
                    var color = subattr;
                } else if (attr === "speed") {
                    var speed = subattr;
                } else if (attr === "mass") {
                    var mass = subattr;
                } else {
                    TypeError("Attribute: " + attr + " not found.");
                }
            }
        }

        
    }
}