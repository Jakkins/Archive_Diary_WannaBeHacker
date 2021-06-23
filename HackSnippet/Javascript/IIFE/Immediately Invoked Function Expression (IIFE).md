[Source - what-is-the-purpose-of-wrapping-whole-javascript-files-in-anonymous-functions](https://stackoverflow.com/questions/2421911/what-is-the-purpose-of-wrapping-whole-javascript-files-in-anonymous-functions-li?noredirect=1)

```javascript
function globalFunction() {
    // code
}
globalFunction();
```
```javascript
(function() {
   var private_var;

   function private_function() {
     //code
   }
})();
```
In the first example, you would explicitly invoke globalFunction by name to run it. That is, you would just do globalFunction() to run it. But in the above example, you're not just defining a function; ```you're defining and invoking it in one go```. This means that when the your JavaScript file is loaded, it is immediately executed.

The behavior would largely be the same except for one significant difference: you avoid polluting the global scope when you use an IIFE (```as a consequence it also means that you cannot invoke the function multiple times since it doesn't have a name```, but since this function is only meant to be executed once it really isn't an issue).

---

```javascript
var myPlugin = (function() {
 var private_var;

 function private_function() {
 }

 return {
    public_function1: function() {
    },
    public_function2: function() {
    }
 }
})()
```
Now you can call myPlugin.public_function1(), but you cannot access private_function()! So pretty similar to a class definition. To understand this better, I recommend the following links for some further reading:
