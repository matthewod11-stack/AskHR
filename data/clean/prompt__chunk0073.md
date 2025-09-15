# Prompt Engineering

deterministic: the highest probability token is always selected (though note that if two tokens have the same highest predicted probability, depending on how tiebreaking is implemented

you may not always get the same output with temperature 0).

Temperatures close to the max tend to create more random output. And as temperature gets

higher and higher, all tokens become equally likely to be the next predicted token.

The Gemini temperature control can be understood in a similar way to the so(cid:454)max function

used in machine learning. A low temperature se(cid:459)ing mirrors a low so(cid:454)max temperature (T),

emphasizing a single, preferred temperature with high ce(cid:457)ainty. A higher Gemini temperature

se(cid:459)ing is like a high so(cid:454)max temperature, making a wider range of temperatures around

the selected se(cid:459)ing more acceptable. This increased unce(cid:457)ainty accommodates scenarios where a rigid, precise temperature may not be essential like for example when experimenting