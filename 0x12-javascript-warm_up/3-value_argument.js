const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('No arguments');
} else {
  console.log(process.argv[2]);
}
