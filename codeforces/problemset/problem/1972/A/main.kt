// https://codeforces.com/problemset/problem/1972/A

fun check(A: List<Int>, B: List<Int>): Boolean {
    for ((i, j) in A.zip(B)) {
        if (i > j) {
            return false
        }
    }
    return true
}

fun main() {
    val t = readln().toInt()
    for (i in 1..t) {
        readln().toInt()
        var A: List<Int> = readln().split(' ').map { it.toInt() }
        var B: List<Int> = readln().split(' ').map { it.toInt() }
        var result = 0
        while (true) {
            if (check(A, B)) {
                println(result)
                break
            } else {
                A = A.dropLast(1)
                A = arrayListOf(0) + A
                A = A.sorted()
                result += 1
            }
        }
    }
}