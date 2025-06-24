#include <iostream>
#include <Eigen/Dense>
#include <nlohmann/json.hpp>
#include <fstream>
using namespace std;
using namespace Eigen;
using json = nlohmann::json;

// Define 128-bit integer matrix type
typedef __int128 int128_t;

// typedef unsigned int uint128_t __attribute__((mode(TI)));

using i128 = int128_t;
using MatrixI128 = Matrix<i128, Dynamic, Dynamic>;

const i128 MOD = (i128)1'000'000'007;

// Fast modular multiplication: A * B using Eigen’s fast GEMM, then reduce mod p
MatrixI128 modmul(const MatrixI128& A, const MatrixI128& B, i128 mod) {
    // Perform fast multiplication
    MatrixI128 C = A * B;
    // Reduce each entry modulo mod
    C = C.unaryExpr([mod](i128 x) { 
        x %= mod;
        if (x < 0) x += mod;
        return x;
    });
    return C;
}

// Fast matrix exponentiation via binary exponentiation
MatrixI128 modpow(MatrixI128 base, long long exp, i128 mod) {
    int n = base.rows();
    MatrixI128 result = MatrixI128::Identity(n, n);
    int c = 0;
    while (exp > 0) {
        cout << "round : " << c++ << ", exp: " << exp << "\n";
        if (exp & 1LL) result = modmul(result, base, mod);
        base = modmul(base, base, mod);
        exp >>= 1;
    }
    return result;
}

// // Helper to print __int128
// ostream& operator<<(ostream& os, i128 x) {
//     if (x == 0) return os << '0';
//     bool neg = x < 0;
//     if (neg) x = -x;
//     string s;
//     while (x) {
//         s += char('0' + (x % 10));
//         x /= 10;
//     }
//     if (neg) os << '-';
//     reverse(s.begin(), s.end());
//     return os << s;
// }



// Load the sparse row format from JSON and convert to full 0/1 matrix
MatrixI128 load_sparse_matrix(const std::string& filename) {
    ifstream infile(filename);
    if (!infile) {
        throw std::runtime_error("Failed to open file: " + filename);
    }

    json j;
    infile >> j;

    // Determine number of rows and infer number of columns from max index
    size_t nrows = 2861;
    size_t ncols = 2861;

    // Create the full matrix with zeros
    MatrixI128 A(nrows, ncols);

    for(int i=0; i<nrows; i++) {
        for(int t=0; t<ncols; t++) {
            A(i, t) = 0;
        }
    }

    // for(int i=0; i<nrows; i++) {
    //     for(int j=0; j<ncols; j++) {
    //         A(i, j) = (i128)((int)A(i, j) + 1LL);
    //     }
    // }

    // Fill in the ones
    for (size_t i = 0; i < nrows; ++i) {
        for (int col : j[i]) {
            i128 value = A(i, col);
            value++;
            A(i,col) = (int)value; 
        }
    }

    return A;
}

void writeMatrixToJsonFile(MatrixI128& matrix, const string& filename) {
    ofstream out(filename);
    if (!out) {
        cerr << "Error opening file: " << filename << endl;
        return;
    }

    out << "[\n";
    for (size_t i = 0; i < 2861; ++i) {
        out << "  [";
        for (size_t j = 0; j < 2861; ++j) {
            out << (int)matrix(i,j);
            if (j + 1 < 2861) out << ", ";
        }
        out << "]";
        if (i + 1 < 2861) out << ",";
        out << "\n";
    }
    out << "]\n";

    out.close();
    cout << "Matrix written to: " << filename << endl;
}


int main() {
    // int n = 3;
    // long long power = 10;

    auto A = load_sparse_matrix("matrix.json");
    cout << "starting\n";
    // for(int i=0; i<n; i++) {
    //     for(int j=0; j<n; j++) {
    //         A(i, j) = 0;
    //     }
    // }

    // A << 1,1,1,
    //      1,0,0,
    //      0,1,0;

    MatrixI128 A_pow = modpow(A, 1000000000000000000, MOD);
    // cout << (int)A_pow(0,0) << "\n";
    cout << "done\n";
    writeMatrixToJsonFile(A_pow, "matrix_answer.json");

    // cout << "A^" << power << " mod " << (long long)1'000'000'007 << " =\n"
    //      << A_pow << endl;

    return 0;
}
