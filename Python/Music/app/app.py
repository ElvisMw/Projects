import os
import sys
import time
import argparse
import essentia.standard as es
from spleeter.separator import Separator
import subprocess
import pyrubberband
from pydub import AudioSegment, effects

# Import AI models for instrument detection, emotion recognition, and audio denoising
from ai_models import InstrumentDetector, EmotionRecognizer, AudioDenoiser

class AudioAnalyzer:
    def __init__(self, input_audio_path):
        self.input_audio_path = input_audio_path
        self.loader = es.MonoLoader(filename=input_audio_path)
        self.audio = self.loader()
    
    def analyze_bpm(self):
        bpm_extractor = es.RhythmExtractor2013(method="multifeature")
        bpm, _ = bpm_extractor(self.audio)
        return bpm
    
    def analyze_key(self):
        key_extractor = es.KeyExtractor()
        key, _ = key_extractor(self.audio)
        return key

    def detect_instruments(self):
        detector = InstrumentDetector()
        instruments = detector.detect(self.input_audio_path)
        return instruments

    def recognize_emotion(self):
        recognizer = EmotionRecognizer()
        emotion = recognizer.recognize(self.input_audio_path)
        return emotion

class AudioProcessor:
    def __init__(self, input_audio_path, output_dir, model_name='spleeter:4stems'):
        self.input_audio_path = input_audio_path
        self.output_dir = output_dir
        self.model_name = model_name
    
    def split_audio(self):
        try:
            # Check if input audio file exists
            if not os.path.exists(self.input_audio_path):
                raise FileNotFoundError(f"Input audio file '{self.input_audio_path}' not found.")

            # Create output directory if it doesn't exist
            os.makedirs(self.output_dir, exist_ok=True)

            # Load separator model
            separator = Separator(self.model_name)

            # Get start time for performance measurement
            start_time = time.time()

            # Perform audio separation
            separator.separate_to_file(self.input_audio_path, self.output_dir,
                                       codec='wav', filename_format='{instrument}.{codec}')

            # Calculate and print processing time
            end_time = time.time()
            processing_time = end_time - start_time
            print(f"Audio separation completed in {processing_time:.2f} seconds.")

        except FileNotFoundError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def pitch_shift(self, semitones):
        # Apply pitch shifting to the input audio file
        output_path = os.path.join(self.output_dir, "pitch_shifted.wav")
        pyrubberband.pitch_shift(self.input_audio_path, output_path, semitones)
        print(f"Pitch shifted audio saved to: {output_path}")

    def time_stretch(self, factor):
        # Apply time stretching to the input audio file
        output_path = os.path.join(self.output_dir, "time_stretched.wav")
        pyrubberband.time_stretch(self.input_audio_path, output_path, factor)
        print(f"Time-stretched audio saved to: {output_path}")

    def apply_audio_effects(self, effect):
        # Apply audio effect to the input audio file
        output_path = os.path.join(self.output_dir, f"{effect}_effect.wav")
        audio = AudioSegment.from_file(self.input_audio_path)
        if effect == "reverb":
            audio = effects.reverb(audio, room_scale=0.5)
        elif effect == "echo":
            audio = effects.echo(audio, delay=100, decay=0.5)
        elif effect == "chorus":
            audio = effects.chorus(audio, voices=3, delay=50, decay=0.5)
        elif effect == "equalize":
            audio = effects.equalize(audio)
        audio.export(output_path, format="wav")
        print(f"{effect.capitalize()} effect applied, saved to: {output_path}")

    def compress_dynamic_range(self):
        # Apply dynamic range compression to the input audio file
        output_path = os.path.join(self.output_dir, "compressed_audio.wav")
        audio = AudioSegment.from_file(self.input_audio_path)
        audio = effects.compress_dynamic_range(audio)
        audio.export(output_path, format="wav")
        print(f"Dynamic range compression applied, saved to: {output_path}")

class AudioFeatureExtractor:
    def __init__(self, input_audio_path):
        self.input_audio_path = input_audio_path
        self.loader = es.MonoLoader(filename=input_audio_path)
        self.audio = self.loader()
    
    def extract_features(self):
        # Example: Extract spectral centroid feature
        spectral_centroid_extractor = es.SpectralCentroid()
        spectral_centroid = spectral_centroid_extractor(self.audio)
        return spectral_centroid

def convert_to_wav(input_media_path):
    # Check the file extension to determine the input format
    _, input_extension = os.path.splitext(input_media_path)
    input_extension = input_extension.lower()

    if input_extension == '.wav':
        # File is already in WAV format
        return input_media_path

    # Generate the output file path with WAV extension
    output_wav_path = os.path.splitext(input_media_path)[0] + '.wav'

    # Use ffmpeg to convert the input media file to WAV format
    command = ['ffmpeg', '-i', input_media_path, '-ac', '2', '-ar', '44100', '-y', output_wav_path]
    try:
        subprocess.run(command, check=True)
        return output_wav_path
    except subprocess.CalledProcessError:
        print("Error: Conversion to WAV format failed.")
        return None

def parse_arguments():
    parser = argparse.ArgumentParser(description="Audio Analysis and Processing Script")
    parser.add_argument("input_audio", help="Input audio file path")
    parser.add_argument("--output_dir", "-o", default="output", help="Output directory for processed files")
    parser.add_argument("--model", "-m", default="spleeter:5stems", help="Spleeter model for audio separation")
    parser.add_argument("--analyze_bpm", action="store_true", help="Analyze BPM of the input audio")
    parser.add_argument("--analyze_key", action="store_true", help="Analyze music key of the input audio")
    parser.add_argument("--split_audio", action="store_true", help="Split audio into stems")
    parser.add_argument("--extract_features", action="store_true", help="Extract audio features")
    parser.add_argument("--detect_instruments", action="store_true", help="Detect instruments in the input audio")
    parser.add_argument("--recognize_emotion", action="store_true", help="Recognize emotion in the input audio")
    parser.add_argument("--denoise_acapella", action="store_true", help="Apply denoising to the generated acapella")
    parser.add_argument("--pitch_shift", type=float,  help="Apply pitch shifting by the specified number of semitones")
    parser.add_argument("--time_stretch", type=float, help="Apply time stretching by the specified factor")
    parser.add_argument("--apply_effect", choices=["reverb", "echo", "chorus", "equalize"], help="Apply audio effect")
    parser.add_argument("--compress_dynamic_range", action="store_true", help="Apply dynamic range compression")
    return parser.parse_args()

def main():
    args = parse_arguments()

    if not os.path.exists(args.input_audio):
        print(f"Error: Input media file '{args.input_audio}' not found.")
        sys.exit(1)

    # Convert media file to WAV format if needed
    input_audio_path = convert_to_wav(args.input_audio)
    if input_audio_path is None:
        print("Error: Conversion to WAV format failed.")
        sys.exit(1)

    # Continue with audio analysis and processing
    if args.analyze_bpm or args.analyze_key:
        analyzer = AudioAnalyzer(input_audio_path)
        if args.analyze_bpm:
            bpm = analyzer.analyze_bpm()
            print(f"BPM: {bpm}")
        if args.analyze_key:
            key = analyzer.analyze_key()
            print(f"Music Key: {key}")

    if args.split_audio:
        processor = AudioProcessor(input_audio_path, args.output_dir, args.model)
        processor.split_audio()

    if args.extract_features:
        feature_extractor = AudioFeatureExtractor(input_audio_path)
        spectral_centroid = feature_extractor.extract_features()
        print(f"Spectral Centroid: {spectral_centroid}")

    if args.detect_instruments:
        analyzer = AudioAnalyzer(input_audio_path)
        instruments = analyzer.detect_instruments()
        print(f"Instruments: {instruments}")

    if args.recognize_emotion:
        analyzer = AudioAnalyzer(input_audio_path)
        emotion = analyzer.recognize_emotion()
        print(f"Emotion: {emotion}")

    if args.denoise_acapella:
        denoiser = AudioDenoiser(input_audio_path)
        cleaned_audio = denoiser.denoise_audio()
        # Save or process the cleaned audio as needed

    if args.pitch_shift:
        processor = AudioProcessor(input_audio_path, args.output_dir)
        processor.pitch_shift(args.pitch_shift)

    if args.time_stretch:
        processor = AudioProcessor(input_audio_path, args.output_dir)
        processor.time_stretch(args.time_stretch)

    if args.apply_effect:
        processor = AudioProcessor(input_audio_path, args.output_dir)
        processor.apply_audio_effects(args.apply_effect)

    if args.compress_dynamic_range:
        processor = AudioProcessor(input_audio_path, args.output_dir)
        processor.compress_dynamic_range()

    # Clean up: delete the temporary WAV file if created
    if input_audio_path != args.input_audio:
        os.remove(input_audio_path)

if __name__ == "__main__":
    main()

