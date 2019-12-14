import torch
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib import font_manager as fm


def translate_sentence(
        sentence,
        src_vocab,
        trg_vocab,
        model,
        device,
        max_len=50
):
    model.eval()

    tokens = ['<sos>'] + sentence + ['<eos>']

    src_indexes = [src_vocab.stoi[token] for token in tokens]

    src_tensor = torch.LongTensor(src_indexes).unsqueeze(0).to(device)

    src_mask = model.make_src_mask(src_tensor)

    with torch.no_grad():
        enc_src = model.encoder(src_tensor, src_mask)

    trg_indexes = [trg_vocab.stoi['<sos>']]

    for i in range(max_len):

        trg_tensor = torch.LongTensor(trg_indexes).unsqueeze(0).to(device)

        trg_mask = model.make_trg_mask(trg_tensor)

        with torch.no_grad():
            output, attention = model.decoder(trg_tensor, enc_src, trg_mask, src_mask)

        pred_token = output.argmax(2)[:, -1].item()

        trg_indexes.append(pred_token)

        if pred_token == trg_vocab.stoi['<eos>']:
            break

    trg_tokens = [trg_vocab.itos[i] for i in trg_indexes]

    return trg_tokens[1:], attention


def get_odia_prop(font_path):
    return fm.FontProperties(fname=font_path)


def display_attention(
        sentence,
        translation,
        attention,
        n_heads=8,
        n_rows=4,
        n_cols=2,
        font_path='fonts/OR51_Ananta.ttf'
):
    assert n_rows * n_cols == n_heads

    fig = plt.figure(figsize=(15, 25))

    for i in range(1, n_heads + 1):
        ax = fig.add_subplot(n_rows, n_cols, i)

        _attention = attention.squeeze(0)[i - 1].cpu().detach().numpy()

        cax = ax.matshow(_attention, cmap='Oranges')

        ax.tick_params(labelsize=12)
        ax.set_xticklabels([''] + ['<sos>'] + sentence + ['<eos>'],
                           rotation=45)
        ax.set_yticklabels([''] + translation,
                           fontproperties=get_odia_prop(font_path))

        ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

    plt.show()
    plt.close()


def tokenize_src(src_str, bpe_src):
    return bpe_src.encode_as_pieces(src_str)


def detokenize_trg(trg_tokens, bpe_trg):
    if trg_tokens[-1] == '<eos>':
        trg_tokens = trg_tokens[:-1]
    return bpe_trg.decode_pieces(trg_tokens)


if __name__ == "__main__":
    from data_utils import load_tokenizers, load_vocab
    from model_utils import load_model

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

    # sample sentence
    sentence = 'music'

    # tokenize
    sentence = tokenize_src(sentence, sp_bpe_src)

    # translate
    translation, attention = \
        translate_sentence(
            sentence,
            SRC_vocab,
            TRG_vocab,
            model,
            model.device
        )

    # detokenize
    print(detokenize_trg(translation, sp_bpe_trg))

    # display attention
    display_attention(sentence, translation, attention)
