//vragen via e-mail of +3256688344

//Hexagons

class Zeshoek{
    constructor(q, r){
        this.q = q
        this.r = r
        return this
    }
    toString(){
        return "Zeshoek(" + this.q.toString() + ", " + this.r.toString() + ")"
    }
    afstand(target){ //input is another class (zeshoek)
        return 0.5*(Math.abs(this.q - target.q) + Math.abs(this.r - target.r) + Math.abs(this.q + this.r - target.q - target.r))
    }
    buur(cardDir){ //Cardinal Direction only
        if (![ "O", "W", "NO", "NW", "ZO", "ZW"].includes(cardDir)){
            throw {
                name: "AssertionError",
                message: "ongeldige richting"
            }
        }
        let tempQ = this.q
        let tempR = this.r
        if (cardDir == "W"){
            tempQ -= 1
        } else if (cardDir == "O"){
            tempQ += 1
        } else if (cardDir == "NO"){
            tempQ += 1
            tempR -= 1
        } else if (cardDir == "NW"){
            tempR -= 1
        } else if (cardDir == "ZO"){
            tempR += 1
        } else if (cardDir == "ZW"){
            tempQ -= 1
            tempR += 1
        }         
        return new Zeshoek(tempQ, tempR)
    }

    pad(pathStr){
        tempQ = this.q
        tempR = this.r
        for (i=0; i<pathStr.length; i++){
            if (["NO", "NW", "ZO", "ZW"].includes(pathStr.slice(i, i+1))){
                if (pathStr == "NO"){
                    tempQ += 1
                    tempR -= 1
                } else if (pathStr == "NW"){
                    tempR -= 1
                } else if (pathStr == "ZO"){
                    tempR += 1
                } else if (pathStr == "ZW"){
                    tempQ -= 1
                    tempR += 1
                }     
                i += 1
                continue
            } else if (["N", "Z"].includes(pathStr[i])){
                throw {
                    name: "AssertionError",
                    message: "ongeldig pad"
                }
            } else {
                if (cardDir == "W"){
                    tempQ -= 1
                } else if (cardDir == "O"){
                    tempQ += 1
                }
            }
        }
    }
}

const tegel = new Zeshoek(0, 0);
console.log(tegel.buur("O").buur("ZO").buur("NO").buur("O").toString())