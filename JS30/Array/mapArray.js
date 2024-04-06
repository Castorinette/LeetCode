/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let mapArray=[];
    var i = 0;
    while (i < arr.length){
        mapArray.push(fn(arr[i],i));
        i++;
    }
    return mapArray;
};

/*Autre solution :

Avec map
var map = function(arr;fn){
    return arr.map(fn);
}
*/