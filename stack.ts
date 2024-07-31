

class Test {
  name: string

  constructor(name: string) {
    this.name = name
  }

  introduceSelf() {
    console.log(`Hi I am ${this.name}`)
  }

}


const test = new Test('test__adv8743ii1')

console.log(test)
test.introduceSelf()
