from vietocr.model.cnn import CNN
from vietocr.model.transformer import LanguageTransformer
from torch import nn

class VietOCR(nn.Module):
    def __init__(self, vocab_size,
                 cnn_args, 
                 transformer_args):
#                 ss=[(2,1), (2,1), (2,1), (2,1), (2,1)], 
#                 ks=[(2,1), (2,1), (1,1), (1,1), (1,1)], 
#                 d_model=512, nhead=8, 
#                 num_encoder_layers=6, num_decoder_layers=6, 
#                 dim_feedforward=2048, max_seq_length=10000, 
#                 pos_dropout=0.1, trans_dropout=0.1):
        
        super(VietOCR, self).__init__()
        
        
#        self.cnn = CNN(**cnn_args)
#        self.transformer=LanguageTransformer(vocab_size, d_model, nhead, num_encoder_layers,
#                                num_decoder_layers, dim_feedforward, max_seq_length,
#                                pos_dropout, trans_dropout)

        self.cnn = CNN(**cnn_args)
        self.transformer=LanguageTransformer(**transformer_args)

    def forward(self, img, tgt_input, tgt_key_padding_mask):
        """
        Shape:
            - img: (N, C, H, W)
            - tgt_input: (T, N)
            - tgt_key_padding_mask: (N, T)
            - output: b t v
        """
        src = self.cnn(img)
        outputs = self.transformer(src, tgt_input, tgt_key_padding_mask=tgt_key_padding_mask)
        
        return outputs

