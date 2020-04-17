// import { Component, Vue, Prop } from 'vue-property-decorator';

// @Component
export default class Greeter {
  public greeting: string = 'abelit';

  public gArr: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

  public newArr: number[] = this.gArr.map((item) => item ** 2).filter((item) => item >= 50);

  constructor(msg: any) {
    // super(msg);
    this.greeting = msg;
    console.log(this.newArr);
  }

  // public greet(): string {
  //   // console.log(this.greeting);
  //   return 'Hello, ' + this.greeting;
  // }
  public greet = () => 'Hello, ' + this.greeting;
}
