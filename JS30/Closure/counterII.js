/*
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        start: init,
        currentValue: init,
        reset() {
            this.currentValue = this.start;
        },
        increment() {
            ++this.currentValue;
        },
        decrement() {
            --this.currentValue;
        }
    }
};


const counter = createCounter(5)
counter.increment(); // 6
console.log(counter.currentValue);
counter.reset(); // 5
console.log(counter.currentValue);
counter.decrement(); // 4
console.log(counter.currentValue);

/*
Autre version : 

var createCounter = function(init) {
    let count = init;

    function increment(){
        return ++count;
    }
    function decrement(){
        return --count;
    }
    function reset()[
        count=init;
        return count;
    ]

    return {
        increment: increment,
        decrement: decrement,
        reset: reset
    }
}
*/