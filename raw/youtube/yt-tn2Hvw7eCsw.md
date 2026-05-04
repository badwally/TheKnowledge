---
id: yt-tn2Hvw7eCsw
type: youtube
title: 'WWDC25: Explore large language models on Apple silicon with MLX | Apple'
url: https://www.youtube.com/watch?v=tn2Hvw7eCsw
authors:
- Apple Developer
ingested_at: '2026-04-30T17:28:26Z'
content_hash: sha256:7778d4195e2697131fa2d722e2986062b7b10058af9bff534b92aa03b96aeed4
domains: []
nlm_corpus_ids: []
wiki_pages: []
meta:
  channel: Apple Developer
  channel_url: https://www.youtube.com/@AppleDeveloper
  duration_seconds: 1200
  caption_track: fetched
  snippet_count: 348
---
[7] Hi, I’m Angelos, 
an engineer in the MLX team.
[10] Today, I’ll show you how MLX is perfect
[13] for large-language 
models on Apple Silicon.
[15] With it, you can perform inference 
and fine-tune massive models
[19] right from your Mac.
[20] And you can do all this with CLI 
applications or from Python or Swift.
[25] If you are new to MLX, it is 
an open-source library
[28] that is purpose-built for doing machine
learning on Apple Silicon.
[31] It utilizes Metal for
acceleration on the GPU
[35] and takes advantage of
unified memory
[37] so that operations on the CPU and GPU 
can work on the same data simultaneously.
[43] You can use MLX in your
favorite language since it provides APIs
[47] in Python, Swift, C++ and even C.
[50] To learn more check out our session
“Get Started with MLX for Apple Silicon”.
[56] When it comes to running large
language models on
[58] on Apple Silicon, MLX unlocks 
powerful new capabilities,
[61] allowing you to run 
the latest state-of-the-art models
[64] right on your Mac with 
a single-line command.
[67] Let’s load DeepSeek AI’s latest model,
[69] which has an impressive
670 billion parameters.
[74] Even when quantized 
to 4.5-bits per weight,
[77] the model’s weights alone still require 
around 380 gigabytes of memory.
[81] To handle that, we're using an M3 Ultra
[83] with its massive 512 gigabytes 
of unified memory,
[87] no other consumer device comes close.
[90] Now that the model is loaded, 
we can start interacting with it.
[93] We can ask it questions like,
[95] “What is the deepest lake 
in the United States?”
[105] Or have it write code for us.
[113] As you can see, MLX enables smooth, 
real-time interaction
[117] and generation at faster 
than reading speeds,
[119] even with models containing 
hundreds of billions of parameters,
[122] all running locally right 
on your Mac desktop.
[125] Now that you've seen what's possible,
let's dive into how you can use MLX
[128] to run these powerful 
models on your own Mac.
[132] We will start by introducing MLX LM, 
a Python library
[135] and a set of command line applications
[137] that can address all of 
your large language model requirements,
[140] providing a robust and versatile solution
[142] for a wide range of applications.
[145] Subsequently, we will delve into text
generation with MLX LM
[148] and show how easy it is to 
generate text either from Python
[151] or from the terminal.
[153] In addition, we will go 
over downloading models
[156] from Hugging Face and quantizing them
for faster inference on device.
[160] MLX can do much more 
than just inference, though.
[163] So next, we will use MLX LM 
to fine tune a language model
[167] on our own data.
[169] In particular, we will train 
a low-rank adapter,
[171] which we can then fuse into 
the model for easier deployment
[174] and faster inference.
[176] Finally, we will go over using
[178] MLX from Swift, where we 
will see how you can
[181] integrate a large language model
[183] in your Swift application with
 only a few lines of code.
[186] The easiest way to get 
started with language models in MLX
[189] is by using MLX LM.
[192] MLX LM is a Python package
 built on top of MLX,
[195] designed for running and experimenting
with large language models.
[199] It provides a set 
of command line tools
[201] that let you generate text 
or fine-tune models
[204] all without writing any code.
[207] And if you do want more control, 
it also provides a Python API
[211] so you can customize the generation
 or training process as much as you like.
[216] It’s also tightly integrated 
with Hugging Face.
[218] That means you can quickly download 
thousands of models from the internet
[222] and even upload your own to 
share with the community.
[225] Getting started is easy; 
just run pip install mlx-lm.
[231] Let's now delve into the details
[232] for the most common use case 
for language models: generating text.
[237] This is a command line tool 
that lets you generate text
[239] using a language model, right from 
your terminal, no code required.
[243] Here’s how it works; you give it a model
[246] from Hugging Face or a local path, 
a text prompt, and it handles the rest.
[251] It downloads the model if needed,
it runs the prompt through it,
[254] and prints the generated response.
[256] So instead of just talking about it, 
let’s run this command.
[271] Within just a few seconds, we get a Swift
implementation of Quick Sort.
[276] You can tweak
the behavior of the model by adding
[278] flags for things like
sampling temperature,
[281] top-p or max tokens, just like with 
any standard text generation setup.
[287] And if you’re curious 
about all the available options,
[289] you can always run 
mlx_lm.generate --help
[294] So whether you’re prototyping ideas,
generating code,
[297] or just exploring what the model can do, 
this is the simplest place to start.
[302] We just saw how easy it 
is to generate text
[304] from the command line 
using mlx_lm.generate.
[307] But one of the real strengths of MLX LM
is that it's not limited to terminal tools.
[312] It also provides a clean
and flexible Python API,
[316] perfect when you want 
more fine-grained control
[318] or need to integrate generation 
into a larger workflow.
[321] Let’s take a look at how we can 
do the same thing,
[324] generating text, using just 
a few lines of Python.
[329] First, we import two utilities;
load and generate.
[333] Load, as the name suggests, handles 
everything  related to model loading.
[337] It fetches the requested model, 
either from your local disk
[340] or directly from Hugging Face
and sets up the model object
[343] along with the tokenizer.
[345] Then we call generate.
[347] This function performs 
a token generation loop
[349] and returns the output text, 
which we can process further
[352] in Python, log, 
or feed into other systems.
[356] So with just these two steps, 
load, then generate,
[359] we get the same functionality as the CLI,
[362] but with full control 
and flexibility in Python.
[365] So here’s another powerful 
aspect of MLX LM’s Python API.
[369] The model you get from load 
isn’t some opaque object
[373] you can only interact with 
through a fixed interface.
[375] It’s a fully structured MLX neural
network, which means you can inspect it,
[380] explore its architecture, 
and even modify it.
[382] Let me show you a quick demo.
[386] We can start by printing the list of 
layers that make up the model.
[390] This gives us a full breakdown of 
the transformer stack, layer by layer.
[394] We can also take a look 
at the model’s parameters,
[397] essentially the weights and biases
that the model has learned.
[409] And if we want to dig into
 a specific part of the network,
[412] say the self-attention module
in the first layer, we can do that too.
[423] This level of transparency 
is really useful,
[425] not just for debugging 
or learning, but also
[428] if you want to experiment 
with things like layer swapping,
[431] custom fine-tuning routines,
or low-level model surgery.
[435] So far, we’ve seen how to 
generate text from a single prompt.
[439] But what if you want to 
maintain a conversation,
[441] or generate responses
 in multiple turns where
[444] each new prompt builds 
on the previous one?
[447] That’s where the key value cache, 
or KV cache, comes in.
[451] Language models use attention 
mechanisms to process
[454] input tokens and during 
generation they repeatedly
[457] compute attention over 
all previously generated tokens.
[460] This can get expensive, especially 
for long prompts or multi-turn scenarios.
[465] A KV cache solves this by storing 
intermediate results from earlier steps,
[470] specifically the keys and values.
[472] Instead of recomputing 
everything from scratch,
[475] the model reuses this cache,  
saving time and computation.
[478] In MLX LM, using 
a KV cache is straightforward.
[483] Let’s update the previous 
Python example
[485] with an explicitly created KV cache that
 we can reuse for multiple generations.
[490] We first create the cache object using
the make_prompt_cache function.
[495] We can use it to 
edit the history in place,
[497] save it for later usage, or swap
between conversations seamlessly.
[502] Then, we pass it into 
the generate function.
[505] And as new tokens are generated, 
the cache gets updated.
[508] Each call continues from 
where the last one left off,
[511] maintaining context across turns.
[514] This is especially useful 
when building chatbots,
[517] virtual assistants, 
or any interactive application
[519] where keeping track of history matters.
[522] Now let’s switch gears a bit 
and talk about model quantization.
[526] We’ve seen how to generate text
and work with models interactively.
[529] But for real-world deployment, efficiency
[531] becomes just as important 
as functionality.
[534] Models are usually released in the same
precision they were trained with,
[538] like float32 or float16.
[541] That is accurate, but it makes them large
and slow, especially on smaller devices.
[546] That's where quantization comes in.
[549] It reduces the model to lower precision, 
like Int8 or even 4-bit,
[553] which reduces memory 
use and speeds up inference,
[556] often with little impact on quality.
[559] But usually, quantization involves 
extra tools, conversion scripts,
[562] and compatibility headaches.
In MLX, it's much simpler.
[568] Quantization is built-in.
[569] You can compress models at various levels
[572] and use them right away for inference
 or training  with no extra setup.
[576] Let's take a look at how this works.
[579] To quantize, or generally convert 
a model with MLX,
[583] you use the mlx_lm.convert command.
[586] This tool takes care of downloading 
a model from Hugging Face,
[589] converting it to a different precision,
and saving it locally all in one step.
[594] In this example, we’re fetching 
the original 16-bit Mistral model
[597] and quantizing it 
to around 4-bits per weight.
[601] The result is a significantly 
smaller model
[603] that’s faster to run 
and requires less memory.
[607] Once converted, the model is saved
to the specified folder and can be used
[611] immediately for inference or training 
using the same MLX LM tools.
[616] And if you want to share 
your quantize model with others,
[619] you can easily upload it back to
[620] Hugging Face by passing 
in a repository name.
[624] So whether you’re optimizing for speed,
[627] saving space, or contributing back 
to the community,
[630] this one command is all you need.
[633] Just like with text generation, 
using the Python API
[636] to convert and quantize models
[638] gives you more flexibility 
without adding complexity.
[641] In fact, MLX LM 
makes it easy to apply
[645] different quantization settings
[646] to different parts of the model 
or from Python.
[650] For example, it’s common 
practice to keep the embedding
[652] and final projection layers
in higher precision
[655] since they tend to be 
more sensitive to quantization.
[658] In this example, we quantize
those layers to 6-bits while the rest of
[662] the model uses 4-bits, striking a great
balance between quality and efficiency.
[667] This is done by passing a quantization 
predicate function, a small function that
[672] receives each layer and returns
the quantization parameters to use for it.
[676] Everything else works exactly the same.
[679] We call convert, pass the Hugging Face path
[681] and local output directory, 
and MLX handles the rest,
[685] including downloading the model
and saving the quantized result.
[689] This fine-grained control 
is especially useful
[692] when you’re experimenting with
model compression or trying to find
[695] the best trade-off between 
performance and accuracy.
[699] So far, we've seen how to generate text
[701] using large language models 
and how to quantize them
[704] for faster inference 
and lighter deployment.
[707] But MLX can do more, especially 
when it comes to training.
[710] With MLX LM, you can fine-tune
a large language model
[713] on your own data right on your Mac,
[715] and crucially, without that 
data ever leaving your device.
[719] And the best part, you can do it without 
writing a single line of code.
[723] Let’s take a look at 
how fine-tuning works.
[726] Large language models are 
usually trained on massive,
[729] general-purpose datasets
from across the Internet.
[732] That gives them broad knowledge,
[734] but it also means they might 
lack depth in specialized domains
[737] or miss the tone
and language of a specific task.
[741] Fine-tuning is how we adapt 
these models to new contexts.
[744] By training them further on a smaller,
[747] domain-specific dataset, 
we can give them new capabilities
[750] or tailor their responses 
to particular needs.
[753] Traditionally, this process 
is done in the cloud,
[756] which can be expensive and often not ideal
[758] when you’re working 
with private or sensitive data.
[762] But with MLX, you can fine-tune 
large language models
[764] locally on your Mac, no cloud required,
and no data ever leaves your machine.
[770] It is efficient, secure, 
and seamlessly integrated
[774] into the MLX workflow.
[776] MLX LM supports two types 
of fine-tuning out of the box:
[780] full model fine-tuning 
and low-rank adapter training.
[783] In full fine-tuning, we update all
 the parameters of the pre-trained model.
[788] This gives you maximum flexibility,
but it's also more resource intensive.
[792] In contrast, adapter training, 
specifically low-rank adapters,
[796] adds a small number of new 
parameters to the model
[799] and trains only those, while
 keeping the original network frozen.
[803] This makes training faster, lighter,
and often more memory efficient,
[808] especially on local hardware.
[810] Let’s look at how we can
 apply this in practice
[812] by fine-tuning the Mistral 
model on a custom dataset.
[816] Let’s take a look at how easy it is
to launch a fine-tuning job with MLX LM.
[821] It only takes a single command
and just a few key arguments.
[825] We specify the model we want to fine-tune,
[827] the path to the dataset, 
and how long we want to train.
[831] Because quantization is deeply 
integrated into MLX,
[834] the mlx_lm.lora command 
can even train adapters
[837] on top of quantized models.
[839] This dramatically reduces memory usage
[841] without sacrificing the ability 
to fine-tune effectively.
[844] In this example, we're training on a 4-bit
quantized version of Mistral,
[848] which cuts memory usage for
the model weights by about 3.5 times
[852] compared to the full precision version.
[854] So even with large models,
fine-tuning remains
[857] practical and efficient right on your Mac.
[860] That single line command
is perfect for a quick training run,
[863] especially when you’re 
just getting started.
[866] But if you want to really 
fine tune performance,
[868] you’ll likely need more control 
over the training process.
[872] That’s where the training 
configuration file comes in.
[875] MLX LM supports config files that give you
fine-grained control
[879] over all aspects of training, 
including path size,
[882] learning rate schedules,
[884] optimizer settings, evaluation intervals,
and more.
[887] This lets you tailor the training setup
[889] to your specific data set, hardware,
or optimization goals,
[893] and get the most out of your adapter.
[895] Let’s now see fine-tuning in action
and how it can update a model’s knowledge.
[900] We start by asking Mistral 7b 
who won the latest Super Bowl.
[912] As expected, the answer is correct, 
but outdated.
[915] The model’s knowledge cutoff means
 it doesn’t have access to recent events.
[919] But the beauty of fine tuning is that
 we can fix this in just a few minutes.
[923] By training on a small dataset 
with questions and answers
[926] about the latest Super Bowl, 
we can update the model’s knowledge
[928] and have it answer accurately.
[939] After just a few minutes of fine-tuning,
the model is now able to respond
[943] with up-to-date answers about teams, 
players, scores and more.
[956] Now that we've trained our adapters,
[958] we can use MLX LM to fuse them 
back into the base model.
[961] This is especially useful for 
deployment and sharing
[964] because it produces a single 
self-contained model
[967] that's easy to distribute and use.
[970] The fusion process combines the adapter
with the original weights,
[974] resulting in a model that has the same 
architecture and number of parameters
[978] as the pre-trained version,
just with updated capabilities.
[982] So from the outside
it behaves like any other model,
[986] but with your fine-tuned 
knowledge built in.
[990] To fuse the adapter into the model,
we use the mlx_lm.fuse command.
[994] It computes the fused weights
[996] and saves the results 
to the specified path, all in one step.
[1000] There’s no need to manually dequantize 
or requantize anything.
[1004] MLX handles that 
automatically and preserves
[1007] the same quantization 
used during training.
[1010] And if you want to share
 your newly fine-tuned model
[1013] with others, it’s just as easy.
[1015] You simply provide
a Huggin Face repository name
[1018] and the fused model will be
 uploaded and ready to use.
[1022] So far, we’ve used Python to generate 
text fine-tune large language models.
[1027] But one of MLX’s standout features is that
[1030] it brings the same simplicity 
and flexibility to Swift.
[1033] Let’s take a look at just 
how easy it is to use
[1036] a large language model in Swift with MLX.
[1039] Here’s a complete example 
of how to load a quantized Mistral model
[1043] and generate text all from Swift.
[1045] And the entire thing 
fits in just 28 lines of code.
[1049] We start by importing MLX 
and the language model libraries.
[1053] Then we create a model container,
[1055] an actor that safely manages concurrent
access to the model and tokenizer.
[1060] Next, we prepare the input.
[1062] We tokenize the prompt,
[1063] converting it into the numerical 
format the model understands.
[1068] Finally, we run the generation loop 
and print the result,
[1071] just like we saw earlier in Python.
It’s the same workflow,
[1075] the same capabilities, 
but now fully native in Swift.
[1079] Let’s now see what it takes 
to retain the history
[1082] of a conversation across 
multiple interactions
[1084] with a model, 
just like we did in Python earlier.
[1087] In Swift, this requires 
just a few extra lines.
[1092] The key idea is the same,
we need to explicitly
[1094] create a key value cache so we can 
reuse it across multiple generations.
[1099] This is done with a single 
additional line of code.
[1101] No complexity added.
[1103] To manage the interaction more precisely,
[1105] we also use a token iterator, 
which allows us
[1108] to set the key value cast directly
and control generations step by step.
[1112] This setup gives us
the flexibility to handle
[1115] multi-turn conversations and advanced 
prompting, all from Swift.
[1120] Throughout this session,
 we’ve seen just how
[1122] simple it is to perform inference, 
training, and quantization with MLX,
[1126] whether through code
or terminal commands.
[1129] Everything we’ve used, 
from the higher-level language model APIs
[1133] down to the Metal kernels that power them,
is fully open-source.
[1136] MLX provides core operations
[1138] in C, C++, Python, and Swift,
with high-level APIs in Python and Swift,
[1145] giving you both flexibility and control
across the entire stack.
[1149] This makes MLX uniquely powerful
for running language models
[1153] and machine learning 
workflows on Apple hardware.
[1156] Let’s now take a look at 
where you can go from here.
[1160] We’ve explored some of
the key features of MLX LM,
[1162] but there’s much more you can do.
[1164] Our documentation dives deeper 
into advanced features
[1167] like distributed inference 
and training, learned quantization,
[1171] and custom training loops.
[1173] To get hands-on quickly, 
the MLX and MLX Swift example repositories
[1177] offer ready-to-run projects for tasks like
[1180] image generation 
with diffusion models,
[1182] speech recognition, 
and full language model training.
[1185] Whether you’re building
 your own AI application
[1188] or exploring under the hood, 
everything you need
[1190] is just a few clicks away to get started.
[1193] We can’t wait to see
the amazing experiences
[1196] you will create on 
Apple hardware using MLX
[1198] and the power of large language models.
