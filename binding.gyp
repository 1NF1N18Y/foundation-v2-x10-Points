{
    "targets": [
        {
            "target_name": "hashing",
            "sources": [
                "hashing.cc",
                "algorithms/sha256d/sha256d.c",
                "algorithms/sha256d/utils/sph_sha2.c",
                "algorithms/main/x10/x10.c",      
                "algorithms/main/common/utils/lyra2.c",
                "algorithms/main/common/utils/sponge.c",
                "algorithms/main/common/utils/sha256c.c",
                "algorithms/main/common/utils/sha256c2.c",
                "algorithms/main/common/utils/utilstrencodings.cpp",
                "algorithms/main/common/sha3/aes_helper.c",
                "algorithms/main/common/sha3/KeccakP-800-reference.c",
                "algorithms/main/common/sha3/sha3.c",
                "algorithms/main/common/sha3/sph_haval.c",
                "algorithms/main/common/sha3/sph_hefty1.c",
                "algorithms/main/common/sha3/sph_fugue.c",
                "algorithms/main/common/sha3/sph_blake.c",
                "algorithms/main/common/sha3/sph_blake2s.c",
                "algorithms/main/common/sha3/sph_bmw.c",
                "algorithms/main/common/sha3/sph_cubehash.c",
                "algorithms/main/common/sha3/sph_echo.c",
                "algorithms/main/common/sha3/sph_gost.c",
                "algorithms/main/common/sha3/sph_groestl.c",
                "algorithms/main/common/sha3/sph_hamsi.c",
                "algorithms/main/common/sha3/sph_jh.c",
                "algorithms/main/common/sha3/sph_keccak.c",
                "algorithms/main/common/sha3/sph_luffa.c",
                "algorithms/main/common/sha3/sph_shavite.c",
                "algorithms/main/common/sha3/sph_simd.c",
                "algorithms/main/common/sha3/sph_skein.c",
                "algorithms/main/common/sha3/sph_whirlpool.c",
                "algorithms/main/common/sha3/sph_shabal.c",
                "algorithms/main/common/sha3/sph_ripemd.c",
                "algorithms/main/common/sha3/sph_sha2.c",
                "algorithms/main/common/sha3/sph_sha2big.c",
                "algorithms/main/common/sha3/sph_tiger.c",
                "algorithms/main/common/cryptonote/cryptonight_dark_lite.c",
                "algorithms/main/common/cryptonote/cryptonight_dark.c",
                "algorithms/main/common/cryptonote/cryptonight_fast.c",
                "algorithms/main/common/cryptonote/cryptonight_lite.c",
                "algorithms/main/common/cryptonote/cryptonight_soft_shell.c",
                "algorithms/main/common/cryptonote/cryptonight_turtle_lite.c",
                "algorithms/main/common/cryptonote/cryptonight_turtle.c",
                "algorithms/main/common/cryptonote/cryptonight.c",
                "algorithms/main/common/crypto/aesb.c",
                "algorithms/main/common/crypto/c_blake256.c",
                "algorithms/main/common/crypto/c_groestl.c",
                "algorithms/main/common/crypto/c_jh.c",
                "algorithms/main/common/crypto/c_keccak.c",
                "algorithms/main/common/crypto/c_skein.c",
                "algorithms/main/common/crypto/hash.c",
                "algorithms/main/common/crypto/oaes_lib.c",
                "algorithms/main/common/crypto/wild_keccak.cpp",
                "algorithms/main/common/ethash/ethash/primes.c",
                "algorithms/main/common/ethash/keccak/keccak.c",
                "algorithms/main/common/ethash/keccak/keccakf800.c",
                "algorithms/main/common/ethash/keccak/keccakf1600.c",          
            ],
            "include_dirs": [
                ".",
                "<!(node -e \"require('nan')\")",
            ],
            "cflags_cc": [
                "-std=c++0x",
                "-fPIC",
                "-fexceptions"
            ],
            "defines": [
                "HAVE_DECL_STRNLEN=1",
                "HAVE_BYTESWAP_H=1"
            ],
            "link_settings": {
                "libraries": [
                    "-Wl,-rpath,./build/Release/",
                ]
            },
            'conditions': [
                ['OS=="mac"', {
                    'xcode_settings': {
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
                    }
                }]
            ]
        }
    ]
}
