import { NewtonianGravity, FindDistance } from "./rules";
import readFile from "fs";

function generate(num, ctx) {
    for (let i = 0; i < num; i++) {
        let x_value = Math.random() * 50;
        let y_value = Math.random() * 50;
        
        const filedata = JSON.parse(readFile('particles.json', (err, data) => {
            if (err) {
                console.log(err);
                return;
            }
            
            return data;
        }))

        
    }
}