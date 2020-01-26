from form_model import InputForm
from flask import Flask, render_template, request
# import torch
from data_utils import load_tokenizers, load_vocab
from model_utils import load_model
from translate_utils import (
    translate_sentence,
    # display_attention,
    tokenize_src,
    detokenize_trg
)

import os
from datetime import datetime

# create app
app = Flask(__name__)


@app.route('/translate', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)

    if request.method == 'POST' and form.validate():

        # tokenize
        sentence = tokenize_src(form.src_text.data, sp_bpe_src)

        # translate
        translation, _ = \
            translate_sentence(
                sentence,
                SRC_vocab,
                TRG_vocab,
                model,
                model.device
            )

        # detokenize
        result = detokenize_trg(translation, sp_bpe_trg)

        """
        # display attention
        display_attention(sentence, translation, attention)
        """
    else:
        result = None

    if result is not None:
        result = f'Odia Translation: {result}'

        if responses_path is not None:
            with open(responses_path, 'a', encoding='utf-8') as _f:
                _f.write(
                    f'\n\tNEW REQUEST 🤩 @'
                    f'{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}\n'
                    f'\tEnglish Text: {form.src_text.data}\n'
                    f'\t{result}\n'
                )

    return render_template(template_name + '.html',
                           form=form, result=result)


if __name__ == '__main__':
    # set template
    template_name = 'my_view'

    # responses dir
    responses_path = 'responses/logs.txt'

    # create responses dir
    os.makedirs('responses', exist_ok=True)

    # set device
    # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    # load tokenizers
    sp_bpe_src, sp_bpe_trg = load_tokenizers(
        'models/bpe_en.model',
        'models/bpe_od.model'
    )

    # load vocab
    SRC_vocab, TRG_vocab = load_vocab(
        'models/SRC_vocab.pkl',
        'models/TRG_vocab.pkl'
    )

    # load model
    model = load_model('models/model.pt', SRC_vocab, TRG_vocab)

    if responses_path is not None:
        with open(responses_path, 'a', encoding='utf-8') as f:
            f.write(
                f'\nstarting app.. '
                f'[{datetime.now().strftime("%m/%d/%Y %H:%M:%S")}]'
                f'\n'
            )

    # run app
    app.run(host='127.0.0.1', port=31137, debug=False)
