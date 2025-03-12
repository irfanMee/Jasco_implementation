from audiocraft.models import JASCO

model = JASCO.get_pretrained('facebook/jasco-chords-drums-400M', chords_mapping_path='assets/chord_to_index_mapping.pkl')

model.set_generation_params(
    cfg_coef_all=7.0,
    cfg_coef_txt=2.0
)

# set textual prompt
text = 'low quality, sustained strings melody, mellow piano melody, sad, soul.'

# run inference
output = model.generate_music(descriptions=[text], chords=None, progress=True)