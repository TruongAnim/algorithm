import kotlin.math.sqrt

fun gcd(a: Int, b: Int): Int {

    val _max = maxOf(a, b)
    for (i in sqrt(_max.toDouble()).toInt() + 1 downTo 1) {
        if (a % i == 0 && b % i == 0) {
            return i
        }
    }
    return 1
}

fun main() {
    val t = readln().toInt()

    for (i in 1..t) {
        var result: Int = 0
        var _max: Int = 0
        val n = readln().toInt()
        for (j in 1..n - 1) {
            val g = gcd(n, j) + j
            if (g > _max) {
                _max = g
                result = j
            }
        }
        println("$result")
    }
}
