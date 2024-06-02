fun progress(n: Int): Int {
    val A = mutableListOf(0, 1, 2, 0, 1, 0, 0, 1)
    if (n <= 7) {
        return A[n]
    } else {
        for (i in 8..n) {
            A.add(minOf(A[i - 1] + 1, A[i - 3], A[i - 5]))
        }
        return A[n]
    }
}

fun main() {
    val t = readln().toInt()
    for (i in 1..t) {
        val n = readln().toInt()
        println(progress(n))
    }
}