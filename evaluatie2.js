//Amazones

class Amazones{
    constructor(){
        this.amazones = {"3-0": "A", "6-0": "a", "0-3": "B", "9-3": "b", "0-6": "C", "9-6": "c", "3-9": "D", "6-9": "d"}
        this.pijlen = []
    }
    toString(){ //create Grid as a baseline pos, then iterate over this.pos and this.pijlen to set positions
        let grid = [["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"],["_","_","_","_","_","_","_","_","_","_"]]
        let output = ""

        for (let i in this.amazones){
            grid[parseInt(i.slice(0,1))][parseInt(i.slice(2,3))] = this.amazones[i]
        }

        for (let i of grid){
            for(let j of i){
                output += j
            }
            output += "\n"
        }
        return output.slice(0,output.length-1)
    }

    positie(amaz){
        for (let i in this.amazones){
            if (amaz == this.amazones[i]){
                return [parseInt(i.slice(0,1)), parseInt(i.slice(2,3))]
            }
        }
    }

    mogelijkeRichtingen(amaz){
        //more complicated, tbd
    }

    winnaar(){
        // this is easy, iterate over all amazones and check their possible moves with mogelijkeRichtingen | if one colour has no possible moves, declare winner else return 0
    }
}

let bord = new Amazones()
console.log(bord.toString())