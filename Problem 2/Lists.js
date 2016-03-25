/**
 * Created by pcannata on 2/27/16.
 */
"use strict";

var list = function() {
    var list = function () {
        function Node(data) {
            this.data = data;
            this.next = null;
        }

        var l = {
            count: 0,
            length: 0,
            currentNode: null,
            head: new Node(null),
            current:null,
            add: function(e) {
                if (l.currentNode === null) { // This is true the first time
                    l.head.data = e;
                    l.currentNode = new Node(null);
                    l.head.next = l.currentNode;
                    l.length++;
                }
                else {
                    l.currentNode.data = e;
                    var node = new Node(null);
                    l.currentNode.next = node;
                    l.currentNode = node;
                    l.length++;
                }
            },
        };

        var F = function () {
        };
        var f = new F();

        // public data
        f.run = function (e) {
            return l[e];
        };
        f.first = f.car = function () {
            return l.head.data
        };
        f.rest = f.cdr = function () {
            if(l.length > 0) {
                l.head = l.head.next;
                l.length--;
            }
            return this;
        }
        f.concat = f.cons = function(e){
            if (typeof e === 'string' || e instanceof String) {l.add(e);}
            else {
                var n = e.run('head');
                for(var i = 0; i < e.run('length'); i++) {
                    l.add(n.data);
                    n = n.next;
                }
            }
        }
        f.length = function(){return l.length};
        f.map = function(f){
            if (f instanceof Function) {
                var n = l.head;
                for(var i = 0; i < l.length; i++) {
                    n.data = f(n.data);
                    n = n.next;
                }
            }
        }
        f.iterate =function(){
            var n = l.current;
            function nextone(){
                if (n == null){
                    l.count += 1;

                    var currentdata = l.head.data;

                    l.current = l.head.next;

                    return currentdata;
                }
                else if (l.count < l.length)   {
                    l.count += 1;
                    var current = n.data;
                    n = n.next;
                    l.current = n;

                    return current;
                }
                else {
                    return null;
                }
            };
            return nextone();
        };

        return f;
    }();
    return list;
};


var l1 = new list();
l1.cons('a')
l1.cons('b')
l1.cons('c')
var h = l1.run('head');
document.writeln("<br>l1 list: " + h.data);
for(var i = 1; i < l1.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}
document.writeln("<br>l1 iterator: " + l1.iterate())
document.writeln("<br>l1 iterator: " + l1.iterate())
document.writeln("<br>l1 iterator: " + l1.iterate())
document.writeln("<br>l1 iterator: " + l1.iterate())
l1.cons("d")
var h = l1.run('head');
document.writeln("<br>l1 new list: " + h.data);
for(var i = 1; i < l1.length(); i++) {
    h = h.next;
    document.writeln(", " + h.data);
}
document.writeln("<br>l1 iterator: " + l1.iterate())
document.writeln("<br>l1 iterator: " + l1.iterate())

